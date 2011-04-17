from generic_api import *

# Simple Python wrapper around the Broadband API provided by the FCC.

APIS = [ ("get_data", "http://api.sba.gov/license_permit/by_business_type/")
       ]

class SBABusinessesApi(GenericAPI):
  def __init__(self):
    GenericAPI.__init__(self, APIS)


# Sample use of BroadbandApi
if __name__ == "__main__":
  bb = SBABusinessesApi()
  print bb.get_data("General Business Licenses") # (Should be San Francisco)