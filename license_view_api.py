from generic_api import *

# Simple Python wrapper around the License View API provided by the FCC.

apis = [ ("get_licenses", "http://data.fcc.gov/api/license-view/basicSearch/getLicenses" )
       ]

# Sample use of BlockConversionAPI
if __name__ == "__main__":
  bc = GenericAPI(apis)
  print bc.get_licenses(searchValue = "Verizon Wireless")