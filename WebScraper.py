from bs4 import BeautifulSoup
import requests
import pandas as pd
import time


def find_cars(number_of_pages, file_number=0):  # Number of pages that you want to loop and file number
    # is just a parameter that changes the csv file name to merge the different files later on

    # DataFrame with all the car and ad info
    df = pd.DataFrame(columns=['Id', 'date', 'title', 'price', 'brand', 'model', 'sub_model', 'version', 'fuel',
                               'register_month', 'register_year', 'number_of_kilometers', 'nr_horses',
                               'seller_location', 'type_of_deal', 'type_of_seller', 'cubic_capacity', 'category',
                               'power',
                               'nr_doors', 'color', 'return_yn', 'loan_yn', 'manual_auto', 'nr_gears', 'no_smoker',
                               'open_ceiling', 'condition', 'co2_emission', 'upholstery', 'wheel_drive'])

    count = 0
    i = 1
    while i != number_of_pages:

        if i == 1:
            url = 'https://www.standvirtual.com/carros/'
            html_text = requests.get(url).text  # Get the html code
            main_soup = BeautifulSoup(html_text, 'lxml')
            ads = main_soup.find_all('article')  # Separate by article tag the ads of cars
        else:  # Change the url for the next pages
            url = "https://www.standvirtual.com/carros/?search%5Border%5D=created_at%3Adesc&page={}".format(i)
            'https://www.standvirtual.com/carros/?search%5Border%5D=created_at%3Adesc&page=498'
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

            price = ad.find('span', class_='offer-price__number ds-price-number')  # price
            if price is not None:
                price = ad.find('span', class_='offer-price__number ds-price-number').text

            seller_location = ad.find('span', class_='ds-location-region')
            if seller_location is not None:
                seller_location = ad.find('span', class_='ds-location-region').text

            type_of_deal = ad.find('span', class_='offer-price__details ds-price-complement')  # Negociable or Fixed
            if type_of_deal is not None:
                type_of_deal = ad.find('span', class_='offer-price__details ds-price-complement').text

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
            id_date_info = car_info.find_all('span', class_='offer-meta__value')
            ad_date = None
            ad_id = None
            if len(id_date_info) != 0:
                ad_date = id_date_info[0].text
            id_info = car_info.find_all('span', class_='offer-meta__value', id="ad_id")
            if len(id_info) != 0:
                ad_id = id_info[0].text

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
                elif specs.span.text == "Emissões CO2":
                    co2_emission = specs.find('div', class_='offer-params__value').text
                elif specs.span.text == "Condição":
                    condition = specs.find('a', class_='offer-params__link').text
                elif specs.span.text == "Estofos":
                    upholstery = specs.find('a', class_='offer-params__link').text
                elif specs.span.text == "Tracção":
                    wheel_drive = specs.find('a', class_='offer-params__link').text
            count += 1  # Count every new car that is checked

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
            print("Number of cars checked: {}".format(count))
        i += 1

    df.to_csv('C:/Users/joaod/Documents/standvirtual_cars{}.csv'.format(file_number))

    # Change your directory, mine is C:/Users/joaod/Documents


if __name__ == '__main__':  # This makes the program loop forever when you press
    file = 0 # Number of the file that is being created
    while True:
        find_cars(100, file)  # I choose to run 100 car pages because I have just loop over the all website
        print("Waiting 12 hours")
        time.sleep(43200)  # Run another cicle after 12 hours
        file += 1
