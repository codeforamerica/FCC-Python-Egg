from generic_api import *
import urllib,json


# Simple Python wrapper around the Broadband API provided by the FCC.

class FRNConversionsAPI(GenericAPI):
  """
  FRNConversionsAPI:
  - an API to access information about broadband provides.
  - original API: http://reboot.fcc.gov/developer/frn-conversions-api
  
  - methods:
    -- getList(stateCode, multi)
       takes stateCode=IL or stateCode=17 (FIPS code),
       (optional) multi=Yes or multi=No to signify whether to include FRNs also operating outside this state.
    
    -- getInfo(frn)
       takes frn='0017855545' (FRN id)
  """


  def __init__(self):
    apis= [
      ('getList', 'http://data.fcc.gov/api/frn/getList'),
      ('getInfo', 'http://data.fcc.gov/api/frn/getInfo')]
      
    GenericAPI.__init__(self,apis)


if __name__ == "__main__":
  bb = FRNConversionsAPI()

  x=bb.getList(stateCode='IL')
  print(type(x))
  print(len(x))
  print(x.keys())

  #print x
  
  print
  x=bb.getInfo(frn='0017855545')
  print(type(x))
  print(len(x))
  print(x)
