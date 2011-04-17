from generic_api import *
import urllib,json


# Simple Python wrapper around the Broadband API provided by the FCC.

class FrnApi(BaseAPIRequest):
  """
  Provides a pythonic abstraction to the API @ http://reboot.fcc.gov/developer/frn-conversions-api

  Two kinds of requests possible:
     1. request(stateCode='IL') or request(stateCode=17) or request(stateCode='IL',multi='No')
         returns a dictionary of FRNs in this state (keyed to 'Frns');
         if multi==Yes, includes FRNs also operating in other states.

     2. request(frn=0017855545)
         returns a dictionary of information about this FRN, keyed to "Info"
  """

  def __init__(self):
    self.url_getList="http://data.fcc.gov/api/frn/getList?stateCode=%s&multi=%s"
    self.url_getInfo="http://data.fcc.gov/api/frn/getInfo?frn=%s"
  

  def format_url(self, **args):
    if 'stateCode' in args:
      self.url=self.url_getList
      #if not 'multi' in args: args['multi']='Yes'
      #self.formatted_url=self.url_getList % (args['stateCode'],args['multi'])
    elif 'frn' in args:
      self.url=self.url_getInfo
      #self.formatted_url = self.url_getInfo % (args['frn'])
    else:
      self.url=self.url_getList
      #print self.url

  def request(self, **args):
    self.format_url(**args)
    BaseAPIRequest.request(self,**args)


# Demonstration of how to use BroadbandApi
if __name__ == "__main__":
  bb = FrnApi()
  #print bb.request(stateCode='IL')

  #exit()
  #x=bb.request_state('IL')
  x=bb.request(stateCode='IL')
  print type(x)
  print len(x)
  print x

  print
  x=bb.request(frn='0017855545')
  print type(x)
  print len(x)
  print x
