from generic_api import *

# Simple Python wrapper around the License View API provided by the FCC.

# The main License View API class. Exposes several API calls as
# functions.

class LicenseViewAPI:
  class GetLicenseAPI(BaseAPIRequest):
    def __init__(self, url):
      self.url = url
    
    def format_url(self, **args):
      self.formatted_url = self.url % (args['search_value'])

    def request(self, **args):
      return BaseAPIRequest.request(self, **args)

  """
  class GetLicenseAPI(BaseAPIRequest):
    def __init__(self, url):
      self.url = url
    
    def format_url(self, **args):
      self.formatted_url = self.url % (args['search_value'])

    def request(self, **args):
      return BaseAPIRequest.request(self, **args)
  """

  def __init__(self):
    self.get_license_api = LicenseViewAPI.GetLicenseAPI("http://data.fcc.gov/api/license-view/basicSearch/getLicenses?searchValue=%s&format=json")

  # Example usage:
  #
  # get_licenses(search_value = "Verizon Wireless")

  def get_licenses(self, **kwargs):
    self.get_license_api.format_url(**kwargs)
    return self.get_license_api.request(**kwargs)


# Sample use of BlockConversionAPI
if __name__ == "__main__":
  bc = LicenseViewAPI()
  print bc.get_licenses(search_value = "Verizon Wireless")