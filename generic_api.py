import urllib
import json

class NoArgumentsException(Exception):
  def __str__(self):
    return "No arguments were found."

class BadJSONException(Exception):
  def __str__(self):
    return "The returned JSON was invalid."


# Perform requests to generic APIs.

class BaseAPIRequest:
  def __init__(self, url):
    self.url = url

  # Formats a URL with the provided keyword arguments. 
  def format_url(self, **args):
    if args is None: raise NoArgumentsException

    args["format"] = "json" #Ask for JSON formatted response
    append = ""

    for arg in args: append += str(arg) + "=" + str(args[arg]) + "&"
    
    append = append[:-1] #Take off last '&'
    self.formatted_url = self.url + "?" + append

  # Requests the API and returns the JSON object.
  def request(self, **args):
    self.format_url(**args)
    #print self.formatted_url
    t = urllib.urlopen(self.formatted_url).read().strip()
    if t.startswith("callback("):
      t=t[t.index("(")+1:-1]

    try:
      return json.loads(t)

    except:
      raise BadJSONException
      return None


class GenericAPI:

  # __init__
  # Parameters: APIS, a list of tuples of form (FUNCTIONNAME, LINK). 
  # 
  # Creates functions of name FUNCTIONNAME that perform an API call to LINK
  # when called, giving back the response as JSON.
  #
  # Returns: Nothing

  def __init__(self, apis):

    self.api_objects   = []
    self.api_functions = []
    self.functions     = []

    # Who writes normal functions when you can use CLOSURES?!?

    number = 0

    # Bind each function to the class.
    for api in apis:
      self.api_objects.append(BaseAPIRequest(api[1]))
      self.bind_closure(number)
      setattr(self, api[0], self.api_functions[number])
      number += 1

  # Creates a function on the current class.
  def bind_closure(self, number):
      def generic_api_call(**kwargs):
        self.api_objects[number].format_url(**kwargs)
        return self.api_objects[number].request(**kwargs)
      
      self.api_functions.append(generic_api_call)