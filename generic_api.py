import urllib
import json

# Inheritable class to perform requests to generic APIs.

class BaseAPIRequest:
  def __init__(self, url):
    self.url = url

  #Inherit this method to describe how to format URLs.
  def format_url(self, **args):
    args["format"] = "json"

    append = ""

    for arg in args:
      append += str(arg) + "=" + str(args[arg]) + "&"
    
    append = append[:-1]

    self.formatted_url = self.url + "?" + append

  # Requests the API and returns the JSON object.
  def request(self, **args):
    self.format_url(**args)
    
    t = urllib.urlopen(self.formatted_url).read().strip()
    if t.startswith("callback("):
      t=t[t.index("(")+1:-1]
    return json.loads(t)
    #object = json.loads("".join([l for l in urllib.urlopen(self.formatted_url)]))
    return object


# Wraps any API that just uses Latitude and Longitude.

class GenericLatLongAPI(BaseAPIRequest):
  def __init__(self, url):
    self.url = url

  def request(self, **args):
    return BaseAPIRequest.request(self, **args)
