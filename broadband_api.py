from generic_api import *

# Simple Python wrapper around the Broadband API provided by the FCC.

class BroadbandApi(GenericLatLongAPI):
  def __init__(self):
    GenericLatLongAPI.__init__(self, "http://data.fcc.gov/api/speedtest/find?latitude=%s&longitude=%s&format=json")



# Sample use of BroadbandApi
if __name__ == "__main__":
  bb = BroadbandApi()
  print bb.request(lat=37, long=-122) # (Should be San Francisco)