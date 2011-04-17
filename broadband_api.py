from generic_api import *

# Simple Python wrapper around the Broadband API provided by the FCC.

class BroadbandApi(GenericLatLongAPI):
  def __init__(self):
    GenericLatLongAPI.__init__(self, "http://data.fcc.gov/api/speedtest/find")



# Sample use of BroadbandApi
if __name__ == "__main__":
  bb = BroadbandApi()
  print bb.request(latitude=37, longitude=-122) # (Should be San Francisco)