import pandas as pd
import numpy as np

df = pd.read_csv('cars_sv_nc.csv', index_col=0)

df.dtypes # Types of variables

# Remove white spaces from title, brand, model, version, type_of_deal,
# type_of_seller, cubic_capacity, category, power, color, return_yn, loan_yn,
# manual_auto, no_smoker, open_ceiling, condition, co2_emission, upholstery, wheel_drive

# Check if there is car ad repeated by id (If there is, removed the repeated ones)

# Change "Fevereiro" and "Março" to "February" and "March", respectively

# Remove "EUR" from price and convert the variable to int

# Remove the column sub_model

# Translate from Portuguese to English the columns fuel, register_month,
# type_of_deal, type_of_seller, category, manual_auto, open_ceiling, condition,
# upholstery, wheel_driver


# Turn this columns to binary: return_yn, loan_yn

# Remove "km" from the column number_of_kilometers and turn it to int

# Remove "cv" from the column power and turn it to int

# Remove "km" from the column number_of_kilometers and turn it to int

# Remove "cm3 " from the column cubic_capacity and turn it to int

# Turn co2_emissions to int

# Remove column nr_horses