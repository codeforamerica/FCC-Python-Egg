from generic_api import *
import urllib,json


# Simple Python wrapper around the Broadband API provided by the FCC.

class FrnApi(BaseAPIRequest):
  def __init__(self):
    self.url_getList="http://data.fcc.gov/api/frn/getList?stateCode=%s&multi=%s"
    self.url_getInfo="http://data.fcc.gov/api/frn/getInfo?frn=%s"
  

  def format_url(self, **args):
    if 'stateCode' in args:
      if not 'multi' in args: args['multi']='Yes'
      self.url=self.url_getList % (args['stateCode'],args['multi'])
    elif 'frn' in args:
      self.url = self.url_getInfo % (args['frn'])
    else:
      self.url = None
    #print self.url

  def request_state(self, stateCode, multi='Yes'):
    #return BaseAPIRequest.request(self, **args)
    url = self.url_getList % (stateCode, multi)
    f = urllib.urlopen(url)
    #return [l for l in f]
    t=f.read().strip()
    
    # jsonp to json
    t=t[t.index('(')+1:-1]

    return json.loads(t)



# Demonstration of how to use BroadbandApi
if __name__ == "__main__":
  bb = FrnApi()
  #print bb.request(stateCode='IL')

  #exit()
  x=bb.request_state('IL')
  print type(x)
  print len(x)
  print x
