from generic_api import *

# Simple Python wrapper around the Block Conversion API provided by the FCC.

class BlockConversionAPI(GenericLatLongAPI):
  def __init__(self):
    GenericLatLongAPI.__init__(self, "http://data.fcc.gov/api/block/find")



# Sample use of BlockConversionAPI
if __name__ == "__main__":
  bc = BlockConversionAPI()
  print bc.request(lat=41, long=-87) # (Should be San Francisco)