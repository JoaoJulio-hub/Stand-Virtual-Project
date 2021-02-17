from bs4 import BeautifulSoup
import requests

i = 1
#while i != 500:

url = 'https://www.standvirtual.com/carros/'
html_text = requests.get(url).text  # Get the html code
main_soup = BeautifulSoup(html_text, 'lxml')
ads = main_soup.find_all('article')  # Separate by article tag the ads of cars

for ad in ads:

    # Get the "basic" data of the ad
    title = ad.find('div', class_="offer-item__title").find('a').text  # Separate by h2 tag, get title of ad
    fuel = ad.find_all('li', class_='ds-param')[0].text  # UList with different information of the ad:
    register_date = ad.find_all('li', class_='ds-param')[1].text
    register_year = ad.find_all('li', class_='ds-param')[2].text
    number_of_kilometers = ad.find_all('li', class_='ds-param')[3].text
    horses = ad.find_all('li', class_='ds-param')[4].text
    price = ad.find('span', class_='offer-price__number ds-price-number').text
    seller_location = ad.find('h4', class_='ds-location hidden-xs').find('span', class_='ds-location-region').text
    type_of_deal = ad.find('span', class_='offer-price__details ds-price-complement').text

    # Get some more detailed data about the car ad
    link = ad.h2.a['href']  # Link to the main page of the ad to get more info
    car_text = requests.get(link).text
    second_soup = BeautifulSoup(car_text, 'lxml')   # Acess the code in the main page of the ad
    car_info = second_soup.find('body')  # Split by body tag just to get all the information we need
    specs_info = car_info.find_all('li', class_='offer-params__item')  # Split by li tag and get all the specs of
    # the car

    # More info of the car ad and initialization of the variables in the case they don't exist in the ads!
    type_announcer = None
    brand = None
    model = None
    sub_model = None
    version = None
    cubic_capacity = None
    power = None
    nr_doors = None
    color = None
    return_yn = None
    loan_yn = None
    car_change = None
    manual_auto = None
    nr_changes = None
    nr_sits = None
    no_smoker = None
    ceiling_open = None
    nr_airbags = None
    condition = None
    nr_airbags = None
    upholstery = None

    for specs in specs_info:
        if specs.span.text == "Anunciante":
            type_announcer = specs.find('a', class_='offer-params__link').text
    print(type_announcer)






