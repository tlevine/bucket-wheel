Bucket-Wheel makes it easier to excavate data from documents.

    from lxml.html import fromstring
    from bucketwheel import PageScraper

    class Menu(PageScraper):
      def download(self):
        return urlopen(self.downloadargs['url']).read()

      def parse(self, page):
        baz = fromstring(page).cssselect('#foo .bar')[0].text_content()
        self.save({"baz": baz}, 'chainsaw')

`PageScraper.save` saves the data in the dictionary plus
the following information

* Download arguments
* Class name
