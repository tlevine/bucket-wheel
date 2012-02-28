def seed(scrapers):
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
    self.__test_is_mapping(downloadargs)
    self.__test_is_mapping(parseargs)
    self.downloadargs = downloadargs
    self.parseargs = parseargs

  @staticmethod
  def __test_is_mapping(a):
    try:
      a.items
      a.keys
      a.values
    except:
      raise TypeError("downloadargs and parseargs must be mapping objects.")


  def pipe(self, objects):
    "Return a list of objects with some added metadata."

    #Check that scrapers is an iterable of PageScraper descendents.

    #Add metadata.
    
    #Return
    return 

class SimpleRequest(PageScraper):
  def __init__(self, *args, **kwargs):
    self.use_cache = kwargs.pop('use_cache') if kwargs.has_key('use_cache') else False
    self.args = args
    self.kwargs = kwargs

  def download(self):
    self.pipe(self.request_func(*self.args,*self.kwargs).content)

class Get(SimpleRequest):
  "Defines `download` so you just have to write `parse`"
  self.request_func = requests.get

class Post(SimpleRequest):
  "Defines `download` so you just have to write `parse`"
  self.request_func = requests.post
