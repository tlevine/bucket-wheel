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
    seed(m1, m2)

`PageScraper.save` saves the data in the dictionary plus
the following information

* Download arguments
* Class name


Blah blah

As you can see, in most cases, you'll just need to define the parse
function for each page time. Then you set no more than a few seed pages
(normally just one seed page), and the bucket-wheel excavator will
run through all of the piped page types.

The bucket-wheel excavator makes it very easy for you to save more
information about the page; the `annotate` function adds metadata,
and helps you cache downloads.

Behind the scenes, the bucket-wheel excavator does some other cool things.

* It pauses random times between page downloads.
* It randomly switches user agents if you do not specify a user agent.
* It stores the scraper progress queue to a file and automatically
resumes from this file.

The `test` method makes it easy to test your scrapers; it allows
you to pass a couple arguments and see what the download and parse
functions do for these particular arguments.
