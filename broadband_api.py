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
    object = json.loads("".join([l for l in urllib.urlopen(self.url)]))
    return object




# Simple Python wrapper around the Broadband API provided by the FCC.
class BroadbandApi(BaseAPIRequest):
  def __init__(self):
    BaseAPIRequest.__init__(self, "http://data.fcc.gov/api/speedtest/find?latitude=%s&longitude=%s&format=json")

  def format_url(self, **args):
    self.url = self.url % (args['lat'], args['long'])

  # Pass in LATitude and LONGitude into this function and get back a JSON object
  # indicating measured broadband speed.
  def request(self, **args):
    return BaseAPIRequest.request(self, **args)


# Demonstration of how to use BroadbandApi
if __name__ == "__main__":
  bb = BroadbandApi()
  print bb.request(lat=37, long=-122) # (Should be San Francisco)