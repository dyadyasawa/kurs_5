
from classes import HeadHunterApi

hh = HeadHunterApi('водоканал')
print(hh.write_to_json(hh.get_employers()))