class PageScraper:
  "Base class for scraping a page"
  def __init__(self, downloadargs, parseargs):
    "Takes two dictionaries"
    try:
      a.items
      a.keys
      a.values
    except:
      raise TypeError("downloadargs and parseargs must be mapping objects.")

    self.downloadargs = downloadargs
    self.parseargs = parseargs
