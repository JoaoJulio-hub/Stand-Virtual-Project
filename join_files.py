import os
import glob
import pandas as pd

# Thanks to freecodebootcamp and Ekapope Viriyakovithya for the code, find the article here:
# https://www.freecodecamp.org/news/how-to-combine-multiple-csv-files-with-8-lines-of-code-265183e0854/

os.chdir("C:/Users/joaod/Documents")  # Choose your directory

extension = 'csv'
all_filenames = [i for i in glob.glob('*.{}'.format(extension))]  # Get all csv files from your directory

# combine all files in the list
combined_csv = pd.concat([pd.read_csv(f) for f in all_filenames])
# export to csv
combined_csv.to_csv("combined_csv.csv", index=False, encoding='utf-8-sig')

print("Done!")
