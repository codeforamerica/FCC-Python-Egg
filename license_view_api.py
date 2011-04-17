from generic_api import *

# Simple Python wrapper around the License View API provided by the FCC.

# The main License View API class. Exposes several API calls as
# functions.

class LicenseViewAPI:
  def __init__(self):
    self.get_license_api = BaseAPIRequest("http://data.fcc.gov/api/license-view/basicSearch/getLicenses")
    self.get_license_api = BaseAPIRequest("http://data.fcc.gov/api/license-view/basicSearch/getLicenses")




  # Example usage:
  #
  # get_licenses(search_value = "Verizon Wireless")

  def get_licenses(self, **kwargs):
    self.get_license_api.format_url(**kwargs)
    return self.get_license_api.request(**kwargs)


# Sample use of BlockConversionAPI
if __name__ == "__main__":
  bc = LicenseViewAPI()
  print bc.get_licenses(searchValue = "Verizon Wireless")