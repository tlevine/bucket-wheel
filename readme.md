Bucket-Wheel makes it easier to excavate data from documents.

    from lxml.html import fromstring
    from bucketwheel import *
    from urllib2 import urlopen
    from highwall import Highwall

    h = Highwall()

    class Menu(PageScraper):
      def download(self):
        self.pipe(urlopen(self.downloadargs['url']).read())

      def parse(self, page):
        x = fromstring(page)
        baz = x.cssselect('#foo .bar')[0].text_content()
        d = self.annotate({"baz": baz})
        h.insert(d, 'chainsaw')
        self.pipe([Docket(url) for url in x.xpath('a/@href')])

    class Docket(Get):
      def parse(self, page):
        x = fromstring(page)
        data= [{"text":p.text_content()} for p in x.cssselect('#main > p')]
        d = self.annotate(data, 'dockets')
        h.insert(d, 'chainsaw')

    m1 = Menu({"url": "http://example.com/foo"})
    m1 = Menu({"url": "http://example.com/bar"})
    seed([m1, m2])

`PageScraper.save` saves the data in the dictionary plus
the following information

* Download arguments
* Class name
