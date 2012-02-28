Bucket-Wheel makes it easier to excavate data from documents.

    from lxml.html import fromstring
    from bucketwheel import *
    from urllib2 import urlopen

    class Menu(PageScraper):
      def download(self):
        self.pipe(urlopen(self.downloadargs['url']).read())

      def parse(self, page):
        x = fromstring(page)
        baz = x.cssselect('#foo .bar')[0].text_content()
        self.save({"baz": baz}, 'chainsaw')
        self.pipe([Docket(url) for url in x.xpath('a/@href')])

    class Docket(Get):
      def parse(self, page):
        x = fromstring(page)
        data= [{"text":p.text_content()} for p in x.cssselect('#main > p')]
        self.save(data, 'dockets')
        self.pipe([Docket(url) for url in x.xpath('a/@href')])

`PageScraper.save` saves the data in the dictionary plus
the following information

* Download arguments
* Class name
