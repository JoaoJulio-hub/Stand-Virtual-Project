from bs4 import BeautifulSoup
from deep_translator import GoogleTranslator
import requests
import pandas as pd

df = pd.DataFrame(columns=['Id', 'date', 'title', 'price', 'brand', 'model', 'sub_model', 'version', 'fuel',
                           'register_month', 'register_year', 'number_of_kilometers', 'nr_horses',
                           'seller_location', 'type_of_deal', 'type_of_seller', 'cubic_capacity', 'category', 'power',
                           'nr_doors', 'color', 'return_yn', 'loan_yn', 'manual_auto', 'nr_gears', 'no_smoker',
                           'open_ceiling', 'condition', 'co2_emission', 'upholstery', 'wheel_drive'])

count = 0
i = 0
while i != 1:

    url = 'https://www.standvirtual.com/carros/'
    html_text = requests.get(url).text  # Get the html code
    main_soup = BeautifulSoup(html_text, 'lxml')
    ads = main_soup.find_all('article')  # Separate by article tag the ads of cars

    if i >= 2:  # Change the url for the next pages
        url = "https://www.standvirtual.com/carros/?search%5Border%5D=created_at%3Adesc&page={}".format(i)
        html_text = requests.get(url).text  # Get the html code
        main_soup = BeautifulSoup(html_text, 'lxml')
        ads = main_soup.find_all('article')  # Separate by article tag the ads of cars

    for ad in ads:

        # Get the "basic" data of the ad
        title = ad.find('div', class_="offer-item__title").find('a').text  # Separate by h2 tag, get title of ad
        fuel = ad.find_all('li', class_='ds-param')[0].text  # UList with different information of the ad:
        register_month = ad.find_all('li', class_='ds-param')[1].text
        register_year = ad.find_all('li', class_='ds-param')[2].text
        number_of_kilometers = ad.find_all('li', class_='ds-param')[3].text
        nr_horses = ad.find_all('li', class_='ds-param')[4].text
        price = ad.find('span', class_='offer-price__number ds-price-number').text
        seller_location = ad.find('h4', class_='ds-location hidden-xs').find('span', class_='ds-location-region').text
        type_of_deal = ad.find('span', class_='offer-price__details ds-price-complement').text  # Negociable or Fixed
        # price

        # Get some more detailed data about the car ad
        link = ad.h2.a['href']  # Link to the main page of the ad to get more info
        car_text = requests.get(link).text
        second_soup = BeautifulSoup(car_text, 'lxml')  # Acess the code in the main page of the ad
        car_info = second_soup.find('body')  # Split by body tag just to get all the information we need
        specs_info = car_info.find_all('li', class_='offer-params__item')  # Split by li tag and get all
        # the specs of the car

        # More info of the car ad and initialization of the variables in the case they don't exist in
        # the ads!

        # Get the info about when the ad was posted and the ID!
        date_id = car_info.find_all('span', class_='offer-meta__value')
        ad_id = date_id[0].text
        ad_date = date_id[1].text
        ad_date = GoogleTranslator(source='portuguese', target='english').translate(ad_date)


        # All specs of the car
        type_seller = None
        brand = None
        model = None
        category = None
        sub_model = None
        version = None
        cubic_capacity = None  # Cilindrada
        power = None
        nr_doors = None
        color = None
        return_yn = None
        loan_yn = None  # Nmr Mudanças
        manual_auto = None  # Tipo de caixa
        nr_gears = None  # Nmr Mudanças
        nr_sits = None  #
        no_smoker = None
        open_ceiling = None
        condition = None
        co2_emission = None
        upholstery = None  # estofo
        wheel_drive = None  # Tracção

        # Get the spefic info of the car:

        for specs in specs_info:
            if specs.span.text == "Anunciante":
                type_seller = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Marca":
                brand = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Modelo":
                model = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Sub-Modelo":
                sub_model = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Versão":
                version = specs.find('div', class_='offer-params__value').text
            elif specs.span.text == "Segmento":
                category = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Cilindrada":
                cubic_capacity = specs.find('div', class_='offer-params__value').text
            elif specs.span.text == "Potência":
                power = specs.find('div', class_='offer-params__value').text
            elif specs.span.text == "Nº de portas":
                nr_doors = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Cor":
                color = specs.find('a', class_='offer-params__link').text
                color = GoogleTranslator(source='portuguese', target='english').translate(color)
            elif specs.span.text == "Aceita retoma":
                return_yn = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Possibilidade de financiamento":
                loan_yn = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Número de Mudanças":
                nr_gears = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Tipo de Caixa":
                manual_auto = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Lotação":
                nr_sits = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Não fumador":
                no_smoker = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Tecto de Abrir":
                open_ceiling = specs.find('a', class_='offer-params__link').text
                open_ceiling = GoogleTranslator(source='portuguese', target='english').translate(open_ceiling)
            elif specs.span.text == "Emissões CO2":
                co2_emission = specs.find('div', class_='offer-params__value').text
            elif specs.span.text == "Condição":
                condition = specs.find('a', class_='offer-params__link').text
            elif specs.span.text == "Estofos":
                upholstery = specs.find('a', class_='offer-params__link').text
                upholstery = GoogleTranslator(source='portuguese', target='english').translate(upholstery)
            elif specs.span.text == "Tracção":
                wheel_drive = specs.find('a', class_='offer-params__link').text
        count += 1
        new_row = {'Id': ad_id, 'date': ad_date, 'title': title, 'price': price, 'brand': brand, 'model': model,
                   'sub_model': sub_model, 'version': version, 'fuel': fuel, 'register_month': register_month,
                   'register_year': register_year, 'number_of_kilometers': number_of_kilometers,
                   'nr_horses': nr_horses, 'seller_location': seller_location, 'type_of_deal': type_of_deal,
                   'type_of_seller': type_seller, 'cubic_capacity': cubic_capacity, 'category': category,
                   'power': power, 'nr_doors': nr_doors, 'color': color, 'return_yn': return_yn, 'loan_yn': loan_yn,
                   'manual_auto': manual_auto, 'nr_gears': nr_gears, 'no_smoker': no_smoker,
                   'open_ceiling': open_ceiling, 'condition': condition, 'co2_emission': co2_emission,
                   'upholstery': upholstery, 'wheel_drive': wheel_drive}
        df = df.append(new_row, ignore_index=True)

        print(df)
        print("Number of cars checked: {}".format(count))
    i += 1
