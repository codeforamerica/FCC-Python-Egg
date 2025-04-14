from generic_api import *

# Simple Python wrapper around the SBA Business API.

def build_api_list(list, base):
  result = []
  for item in list:
    result.append((item, base + "/" + item + "/" ))
  
  return result


#These are the function calls that the SBABusinessesAPI object exposes.
list = [ "by_category"
       , "all_by_state"
       , "by_business_type"
       , "state_only"
       , "state_and_county"
       , "state_and_city"
       , "by_zip"
       ]

APIS = build_api_list(list, "http://api.sba.gov/license_permit")

class SBABusinessesAPI(GenericAPI):
  def __init__(self):
    GenericAPI.__init__(self, APIS)


# Sample use of BroadbandApi
if __name__ == "__main__":
  bb = SBABusinessesAPI()
  print(bb.by_category("doing business as")) # (Should be San Francisco)
