from generic_api import *

# Simple Python wrapper around the SBA Business API.

def build_api_list(list, base):
  result = []
  for item in list:
    result.append((item, base + "/" + item + "/" ))
  
  return result


#These are the function calls that the SBABusinessesAPI object exposes.
list = [ "federal"
       , "state_financing_for"
       , "federal_and_state_financing_for"
       # , "nil/for_profit"
       # , "nil/for_profit/nil" #What were they thinking?!
       # , "nil/for_profit"
       # STATE ABBREVIATION/for_profit/nil/SPECIALTY
       # STATE ABBREVIATION/for_profit/nil/SPECIALTY1-SPECIALTY2- ... SPECIALTYN
       # STATE ABBREVIATION/for_profit/INDUSTRY/SPECIALTY
       ]

APIS = build_api_list(list, "http://api.sba.gov/loans_grants")

class SBALoansGrantsAPI(GenericAPI):
  def __init__(self):
    GenericAPI.__init__(self, APIS)


# Sample use of BroadbandApi
if __name__ == "__main__":
  bb = SBALoansGrantsAPI()
  print(bb.by_category("doing business as")) # (Should be San Francisco)
