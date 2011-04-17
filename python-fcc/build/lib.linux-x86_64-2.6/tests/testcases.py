import sys
import unittest

sys.path.append('../')

from broadband_api import *
from FRNConversionsAPI import *
from block_conversion_api import *

class TestBroadbandAPI (unittest.TestCase):
  def setUp(self):
    self.bb = BroadbandApi()
    self.frnapi = FRNConversionsAPI()
  

  #Sweep across the US and compare to precomputed values.
  def test_Sweep(self):

    # The following is how I computed the values beforehand:

    # print "results = "
    # print "[",
    # for x in range(10):
    #   print self.bb.request(latitude=41, longitude=-86 + x * 10)['status'] == 'OK', ",", 
    # print "]"
    results = [ True , True , False , False , False , False , False , False , False , False , ]

    for x in range(10):
      self.assertTrue((self.bb.get_data(latitude=41, longitude=-86 + x * 10)['status'] == 'OK') == results[x])


  # Does SF exist?
  def test_SF(self):
    result = self.bb.get_data(latitude=37, longitude=-122)

    self.assertTrue(result['status'] == 'OK')
    self.assertTrue('SpeedTestCounty' in result)
  
  # Does Chicago exist?
  def test_Chicago(self):
    result = self.bb.get_data(latitude=41, longitude=-87)

    self.assertTrue(result['status'] == 'OK')


  # Test the middle of nowhere (Disclaimer: I have no idea where 
  # this is, so it may not be in the middle of nowhere)
  def test_Nowhere(self):
    result = self.bb.get_data(latitude=35, longitude=35)
    
    self.assertTrue(result['status'] == 'Fail')

  def test_FRN(self):
    result = self.frnapi.getInfo(frn='0017855545')
    self.assertTrue(result['Info']['frn'] == '0017855545')

  def test_companyName(self):
    result = self.frnapi.getInfo(frn='0017855545')
    self.assertTrue(result['Info']['companyName']=='Cygnus Telecommunications Corporation')
  
  def test_FRNapiIsDict(self):
    result1 = self.frnapi.getList(stateCode='IL')
    result2 = self.frnapi.getInfo(frn='0017855545')
    self.assertTrue(type(result1)==type({}) and type(result2)==type({}))
  def test_CygnusInIL(self):
    result = self.frnapi.getList(stateCode='IL')
    #print result['Frns']
    #Cygnus Telecommunications Corporation
    self.assertTrue('Cygnus Telecommunications Corporation' in [x['companyName'] for x in result['Frns']['Frn']])

  





class TestBlockConversionAPI (unittest.TestCase):
  def setUp(self):
    self.bb = BlockConversionAPI()

  # Does SF exist?
  def test_SF(self):
    result = self.bb.get_block(latitude=37, longitude=-122)

    self.assertTrue(result['status'] == 'OK')
    self.assertTrue(result['State']['code'] == 'CA')
    self.assertTrue(result['Block']['FIPS'] == '060871001001002C')


  # Does (somewhere near) Chicago exist?
  def test_Chicago(self):
    result = self.bb.get_block(latitude=41, longitude=-87)

    self.assertTrue(result['Block']['FIPS'] == '180739908004112')


  # Test the middle of nowhere (Disclaimer: I have no idea where 
  # this is, so it may not be in the middle of nowhere)
  def test_Nowhere(self):
    result = self.bb.get_block(latitude=35, longitude=35)
    
    self.assertTrue(result['status'] == 'Fail')

if __name__ == '__main__':
    unittest.main()
