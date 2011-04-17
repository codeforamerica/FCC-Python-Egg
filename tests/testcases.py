import sys
import unittest

sys.path.append('../')

from broadband_api import *
from block_conversion_api import *

class TestBroadbandAPI (unittest.TestCase):
  def setUp(self):
    self.bb = BroadbandApi()
  

  #Sweep across the US and compare to precomputed values.
  def test_Sweep(self):

    # The following is how I computed the values beforehand:

    # print "results = "
    # print "[",
    # for x in range(10):
    #   print self.bb.request(lat=41, long=-86 + x * 10)['status'] == 'OK', ",", 
    # print "]"
    results = [ True , True , False , False , False , False , False , False , False , False , ]

    for x in range(10):
      self.assertTrue((self.bb.request(lat=41, long=-86 + x * 10)['status'] == 'OK') == results[x])


  # Does SF exist?
  def test_SF(self):
    result = self.bb.request(lat=37, long=-122)

    self.assertTrue(result['status'] == 'OK')
    self.assertTrue('SpeedTestCounty' in result)
  
  # Does Chicago exist?
  def test_Chicago(self):
    result = self.bb.request(lat=41, long=-87)

    self.assertTrue(result['status'] == 'OK')


  # Test the middle of nowhere (Disclaimer: I have no idea where 
  # this is, so it may not be in the middle of nowhere)
  def test_Nowhere(self):
    result = self.bb.request(lat=35, long=35)
    
    self.assertTrue(result['status'] == 'Fail')




class TestBlockConversionAPI (unittest.TestCase):
  def setUp(self):
    self.bb = BlockConversionAPI()

  # Does SF exist?
  def test_SF(self):
    result = self.bb.request(lat=37, long=-122)

    self.assertTrue(result['status'] == 'OK')
    self.assertTrue(result['State']['code'] == 'CA')
    self.assertTrue(result['Block']['FIPS'] == '060871001001002C')


  # Does (somewhere near) Chicago exist?
  def test_Chicago(self):
    result = self.bb.request(lat=41, long=-87)

    self.assertTrue(result['Block']['FIPS'] == '180739908004112')


  # Test the middle of nowhere (Disclaimer: I have no idea where 
  # this is, so it may not be in the middle of nowhere)
  def test_Nowhere(self):
    result = self.bb.request(lat=35, long=35)
    
    self.assertTrue(result['status'] == 'Fail')

if __name__ == '__main__':
    unittest.main()
