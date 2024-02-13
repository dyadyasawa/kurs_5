
from classes import HeadHunterApi
from pprint import pprint

''' employers_id = [
                   '1327757',
                   '1244626',
                   '1302763',
                   '671067',
                   '8957756',
                   '31480',
                   '723727',
                   '3948330',
                   '1455',
                   '2840576'
                   '3637300'
                   '189683'
                   '2221824'
                   '71895'
                   ] '''

hh = HeadHunterApi()
# pprint(hh.get_employers())
hh.write_to_json()
pprint(hh.choice_from_json())

