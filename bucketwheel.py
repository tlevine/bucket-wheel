def queue(scrapers):
  """Takes a scraper object or a list of scraper objects.
  Run these scraper objects and any piped objects."""
  while len(scrapers) > 0:
    scraper = scrapers.pop()
    page = scraper.download()
    morescrapers = scraper.parse(page)
    scrapers.append(morescrapers)

class PageScraper:
  "Base class for scraping a page"
  def __init__(self, downloadargs, parseargs, usecache = True):
    "Takes two dictionaries"
    try:
      a.items
      a.keys
      a.values
    except:
      raise TypeError("downloadargs and parseargs must be mapping objects.")

    self.downloadargs = downloadargs
    self.parseargs = parseargs

  def pipe(self, scrapers):
    "Return a list of scraper objects with some metadata."

    #Check that scrapers is an iterable of PageScraper descendents.

    #Add metadata.
    
    #Return
    return 
