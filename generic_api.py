import urllib
import json

class NoArgumentsException(Exception):
  def __str__(self):
    return "No arguments were found."

class BadJSONException(Exception):
  def __str__(self):
    return "The returned JSON was invalid."


# Inheritable class to perform requests to generic APIs.

class BaseAPIRequest:
  def __init__(self, url):
    self.url = url

  #Inherit this method to describe how to format URLs.
  def format_url(self, **args):
    if args is None:
      raise NoArgumentsException

    args["format"] = "json" #Ask for JSON formatted response
    append = ""

    for arg in args: append += str(arg) + "=" + str(args[arg]) + "&"
    
    append = append[:-1] #Take off last '&'
    self.formatted_url = self.url + "?" + append

  # Requests the API and returns the JSON object.
  def request(self, **args):
    self.format_url(**args)
    #print self.formatted_url
    t = urllib.urlopen(self.formatted_url).read().strip()
    if t.startswith("callback("):
      t=t[t.index("(")+1:-1]
    
    try:
      return json.loads(t)
    except:
      raise BadJSONException
      return None

    #object = json.loads("".join([l for l in urllib.urlopen(self.formatted_url)]))


# Wraps any API that just uses Latitude and Longitude.

#TODO: This is no longer necessary...
class GenericLatLongAPI(BaseAPIRequest):
  def __init__(self, url):
    self.url = url

  def request(self, **args):
    return BaseAPIRequest.request(self, **args)
