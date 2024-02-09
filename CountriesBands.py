import pytesseract
from PIL import Image
import requests
import pycountry
import re

def normalize_string(cos):
    return re.sub(r'[^a-zA-Z]', '', cos)


def read_text_from_image(image_path):
    pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'
    try:
        text = pytesseract.image_to_string(Image.open(image_path))
        return text
    except Exception as e:
        return f"Błąd podczas odczytywania obrazu: {e}"

def find_country_in_text(text):
    for country in pycountry.countries:
        if country.name.upper() in text.upper():
            return country_name
    return None

def get_country_info(country_name):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/name/{country_name}", timeout=30)
        if response.status_code == 200:
            country_data = response.json()[0]
            return {
                'Stolica': country_data['capital'][0],
                'Waluta': country_data['currencies'][list(country_data['currencies'].keys())[0]]['name'],
                'Populacja': country_data['population'],
                'Flaga': country_data['flags']['png']
            }
        else:
            return "Nie znaleziono informacji o kraju."
    except requests.exceptions.RequestException as e:
        return f"Błąd podczas pobierania danych: {e}"


image_path = r'c:\www\ND.png'
country_name = read_text_from_image(image_path)
country_name = normalize_string(country_name)

if country_name:
    print(f"Odczytano nazwę kraju: {country_name}")
    country_info = get_country_info(country_name)
    print(f"Informacje o kraju {country_name}:")
    print(country_info)
else:
    print("Nie udało się odczytać tekstu z obrazu.")


print(f"Requesting URL: https://restcountries.com/v3.1/name/{country_name}")


