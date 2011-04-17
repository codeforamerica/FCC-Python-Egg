import sys
sys.path.append('../')

import unittest
from broadband_api import *
from frn_api import *

class TestBroadbandAPI (unittest.TestCase):

  def setUp(self):
    self.bb = BroadbandApi()
    self.frnapi = FrnApi()
  

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

  def test_FRN(self):
    result = self.frnapi.request(frn='0017855545')
    self.assertTrue(result['Info']['frn'] == '0017855545')

  def test_companyName(self):
    result = self.frnapi.request(frn='0017855545')
    self.assertTrue(result['Info']['companyName']=='Cygnus Telecommunications Corporation')
  
  def test_FRNapiIsDict(self):
    result1 = self.frnapi.request(stateCode='IL')
    result2 = self.frnapi.request(frn='0017855545')
    self.assertTrue(type(result1)==type({}) and type(result2)==type({}))
  def test_CygnusInIL(self):
    result = self.frnapi.request(stateCode='IL')
    #print result['Frns']
    #Cygnus Telecommunications Corporation
    self.assertTrue('Cygnus Telecommunications Corporation' in [x['companyName'] for x in result['Frns']['Frn']])

  



if __name__ == '__main__':
    unittest.main()
