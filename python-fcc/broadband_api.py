from generic_api import *

# Simple Python wrapper around the Broadband API provided by the FCC.

APIS = [("get_data", "http://data.fcc.gov/api/speedtest/find")]

class BroadbandApi(GenericAPI):
  def __init__(self):
    GenericAPI.__init__(self, APIS)


# Sample use of BroadbandApi
if __name__ == "__main__":
  bb = BroadbandApi()
  print(bb.get_data(latitude=37, longitude=-122)) # (Should be San Francisco)
