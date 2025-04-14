import urllib
import json

class NoArgumentsException(Exception):
  def __str__(self):
    return "No arguments were found."

class BadJSONException(Exception):
  def __str__(self):
    return "The returned JSON was invalid."

class NonexistentStyleException(Exception):
  def __str__(self):
    return "The requested API style was invalid."

class MustBeOrderedException(Exception):
  def __str__(self):
    return "The arguments you pass to the SBA API must be ordered."


# Perform requests to generic APIs.

PHP_STYLE = 0 # &x=1&y=2
SBA_WEIRD_STYLE = 1

class BaseAPIRequest:
  def __init__(self, url):
    self.url = url

    if self.url.startswith("http://api.sba.gov") or self.url.startswith("api.sba.gov"):
      self.api_style = SBA_WEIRD_STYLE
    else:
      self.api_style = PHP_STYLE

  def __format_url_php_style(self, *ordered_args, **args):
    """
    Format the url with the arguments in PHP style. That is, 
    ?x=5&y=6
    """
    if args is None: raise NoArgumentsException

    args["format"] = "json" #Ask for JSON formatted response
    append = ""

    for arg in args: append += str(arg) + "=" + str(args[arg]) + "&"
    
    append = append[:-1] #Take off last '&'
    self.formatted_url = self.url + "?" + append

  def __format_url_weird_style(self, *ordered_args, **args):
    """
    Format the url with the arguments in the weird style given by SBA.
    arg1/arg2/arg3.json
    """

    append = ""
    for arg in ordered_args: append += str(arg) + "/"
    append = append[:-1] #Take off last '/'


    self.formatted_url = self.url + append + ".json"

  # Formats a URL with the provided keyword arguments. 
  def format_url(self, *ordered_args, **args):
    if self.api_style == PHP_STYLE:
      self.__format_url_php_style(*ordered_args, **args)
    elif self.api_style == SBA_WEIRD_STYLE:
      print(ordered_args)
      print(args)
      if len(args) != 0:
        raise MustBeOrderedException # MUST be ordered.
      
      self.__format_url_weird_style(*ordered_args) 
    else:
      raise NonexistentStyleException

  # Requests the API and returns the JSON object.
  def request(self, *ordered_args, **args):
    self.format_url(*ordered_args, **args)
    #print self.formatted_url
    t = urllib.request.urlopen(self.formatted_url).read().strip()
    if t.startswith(b"callback("):
      t=t[t.index("(")+1:-1]

    print(self.formatted_url)

    try:
      return json.loads(t)

    except:
      raise BadJSONException
      return None


class GenericAPI:

  """
  __init__
  Parameters: APIS, a list of tuples of form (FUNCTIONNAME, LINK). 
  
  Creates functions of name FUNCTIONNAME that perform an API call to LINK
  when called, giving back the response as JSON.
  
  Returns: Nothing
  """

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
      def generic_api_call(*ordered_args, **kwargs):
        self.api_objects[number].format_url(*ordered_args, **kwargs)
        return self.api_objects[number].request(*ordered_args, **kwargs)
      
      self.api_functions.append(generic_api_call)
