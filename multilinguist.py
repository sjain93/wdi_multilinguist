import requests
import json
import random

class Multilinguist:
  """This class represents a world traveller who knows
  what languages are spoken in each country around the world
  and can cobble together a sentence in most of them
  (but not very well)
  """

  translatr_base_url = "http://bitmakertranslate.herokuapp.com"
  countries_base_url = "https://restcountries.eu/rest/v2/name"
  #{name}?fullText=true
  #?text=The%20total%20is%2020485&to=ja&from=en

  def __init__(self):
    """Initializes the multilinguist's current_lang to 'en'

    Returns
    -------
    Multilinguist
        A new instance of Multilinguist
    """
    self.current_lang = 'en'

  def language_in(self, country_name):
    """Uses the RestCountries API to look up one of the languages
    spoken in a given country

    Parameters
    ----------
    country_name : str
         The full name of a country.

    Returns
    -------
    bool
        2 letter iso639_1 language code.
    """
    params = {'fullText': 'true'}
    response = requests.get(f"{self.countries_base_url}/{country_name}", params=params)
    json_response = json.loads(response.text)
    return json_response[0]['languages'][0]['iso639_1']

  def travel_to(self, country_name):
    """Sets current_lang to one of the languages spoken
    in a given country

    Parameters
    ----------
    country_name : str
        The full name of a country.

    Returns
    -------
    str
        The new value of current_lang as a 2 letter iso639_1 code.
    """
    local_lang = self.language_in(country_name)
    self.current_lang = local_lang
    return self.current_lang

  def say_in_local_language(self, msg):
    """(Roughly) translates msg into current_lang using the Transltr API

    Parameters
    ----------
    msg : str
        A message to be translated.

    Returns
    -------
    str
        A rough translation of msg.
    """
    params = {'text': msg, 'to': self.current_lang, 'from': 'en'}
    response = requests.get(self.translatr_base_url, params=params)
    json_response = json.loads(response.text)
    # print(response.status_code)
    # print(json_response)
    return json_response['translationText']


class Math_genius(Multilinguist):

    def __init__(self):
        super(). __init__()

    def report_total(self, num_list = []):
        self.num_list = num_list
        math_sum = sum(self.num_list)
        return self.say_in_local_language("The total is {}".format(math_sum))

me = Math_genius()
print(me.report_total([23,45,676,34,5778,4,23,5465]))
me.travel_to("India")
print(me.report_total([6,3,6,68,455,4,467,57,4,534]))

class Quote_collector(Multilinguist):
    quotes = []

    def __init__(self):
        super(). __init__()

    def quote_add(self, new_quote):
        self.new_quote = str(new_quote)
        cls.quotes.append(self.new_quote)

    def quote_translate(self):
        """Taking a random quote from the quote list and translating it based on local_lang"""
        to_translate = cls.quotes.random.choice()

        if self.local_lang == "en":
            return "{}".format(to_translate)
        else:
            return self.say_in_local_language("{}".format(to_translate))

hobo = Quote_collector()
hobo.quote_add("To be or not to be that is the question")
hobo.travel_to("India")
print(hobo.quote_translate())
