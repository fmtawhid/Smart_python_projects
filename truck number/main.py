import phonenumbers
from number import num
from phonenumbers import geocoder
from phonenumbers import parse
pepnumber = phonenumbers.parse(num)
location = geocoder.description_for_number(pepnumber, 'en')
print(location)
from phonenumbers import carrier
dervice_pro = phonenumbers.parse(num)
print(carrier.name_for_number(dervice_pro, "en"))