
from classes import HeadHunterApi
from pprint import  pprint

hh = HeadHunterApi('и')
hh.write_to_json()
pprint(hh.choice_from_json())

