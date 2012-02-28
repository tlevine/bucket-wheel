Bucket-Wheel makes it easier to excavate data from documents.

    from lxml.html import fromstring
    from bucketwheel import *

    class Menu(PageScraper):
      def download(self):
        self.pipe(urlopen(self.downloadargs['url']).read())

      def parse(self, page):
        x = fromstring(page)
        baz = x.cssselect('#foo .bar')[0].text_content()
        self.save({"baz": baz}, 'chainsaw')
        self.pipe([Docket(url) for url in x.xpath('a/@href')])

    class Docket(GetURL):

`PageScraper.save` saves the data in the dictionary plus
the following information

* Download arguments
* Class name
