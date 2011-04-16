import urllib
import json

# Inheritable class to perform requests to generic APIs.
class BaseAPIRequest:
  def __init__(self, url):
    self.url = url

  #Inherit this method to describe how to format URLs.
  def format_url(self):
    pass

  # Requests the API and returns the JSON object.
  def request(self, **args):
    self.format_url(**args)
    object = json.loads("".join([l for l in urllib.urlopen(self.formatted_url)]))
    return object
