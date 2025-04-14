from .generic_api import *

# Simple Python wrapper around the License View API provided by the FCC.

APIS = [ ("get_licenses", "http://data.fcc.gov/api/license-view/basicSearch/getLicenses" )
       , ("get_common_names", "http://data.fcc.gov/api/license-view/licenses/getCommonNames")
       , ("get_statuses", "http://data.fcc.gov/api/license-view/licenses/getStatuses")
       , ("get_categories", "http://data.fcc.gov/api/license-view/licenses/getCategories")
       , ("get_entities", "http://data.fcc.gov/api/license-view/licenses/getEntities")
       , ("get_renewals", "http://data.fcc.gov/api/license-view/licenses/getRenewals")
       , ("get_issued", "http://data.fcc.gov/api/license-view/licenses/getIssued")
       ]


class LicenseViewAPI(GenericAPI):
  def __init__(self):
    GenericAPI.__init__(self, APIS)

# Sample use of BlockConversionAPI
if __name__ == "__main__":
  bc = LicenseViewAPI()
  print(bc.get_licenses(searchValue = "Verizon Wireless"))
