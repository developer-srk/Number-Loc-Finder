import phonenumbers
from phonenumbers import geocoder
phone_number1 = phonenumbers.parse("+911121222")

print("/nPhone Number Location/n")
print(geocoder.description_for_number(phone_number1,"en"))
