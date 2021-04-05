import phonenumbers
from test import number

from phonenumbers import geocoder

CN_number = phonenumbers.parse(number, "CN")
print(geocoder.description_for_number(CN_number, 'en'))

from phonenumbers import carrier

SP_number = phonenumbers.parse(number, "SP")
print(carrier.name_for_number(SP_number, "en"))