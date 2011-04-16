import urllib
import json

class BaseAPIRequest:
  def __init__(self):
    pass
  
  def request(self, **args):
    pass

# Simple Python wrapper around the Broadband API provided by the FCC.
class BroadbandApi(BaseAPIRequest):
  def __init__(self):
    pass

  # Pass in LATitude and LONGitude into this function and get back a JSON object
  # indicating measured broadband speed.
  def request(self, **args):
    url = "http://data.fcc.gov/api/speedtest/find?latitude=%s&longitude=%s&format=json"
    url = url % (args['lat'], args['long'])

    object = json.loads("".join([l for l in urllib.urlopen(url)]))
    return object


# Demonstration of how to use BroadbandApi
if __name__ == "__main__":
  bb = BroadbandApi()
  print bb.request(lat=37, long=-122) # (Should be San Francisco)