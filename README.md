# Phone-Loc-Finder

**Phone-Loc-Finder** is a Python-based tool that identifies the geographical location of a phone number. It leverages the `phonenumbers` library to parse and extract location data in a user-friendly format. This lightweight script is ideal for basic location-based queries for phone numbers.

## Features
- Parses phone numbers in international format.
- Displays the geographical region associated with the phone number.
- Simple and straightforward implementation using the `phonenumbers` library.

## How It Works
1. Parses the phone number using the `phonenumbers` library.
2. Uses the `geocoder` module to extract and display the location in English.

## Example Usage
```python
import phonenumbers
from phonenumbers import geocoder

phone_number = phonenumbers.parse("+917620014422")

print("\nPhone Number Location\n")
print(geocoder.description_for_number(phone_number, "en"))
