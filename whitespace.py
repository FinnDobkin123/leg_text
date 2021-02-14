#Import libraries
import pandas as pd
import csv
import statistics

#Read file in as a dataframe
url = 'https://github.com/FinnDobkin123/leg_text/blob/main/congress.csv'
congress_file = pd.read_csv(url, index_col = 0)
congress_df = pd.DataFrame(data = congress_file)
congress_df.head(5)
congress = open('congress_df', 'r')

#Read data in with open
import csv
import statistics
with open('bills.csv', 'r') as bill_file:
    fieldnames = ['bill_number', 'congress', 'bill_title', 'bill_subtitle']
    csv_reader = csv.DictReader(bill_file, delimiter = ',', skipinitialspace=True, 
                               fieldnames = fieldnames)
    for row in bill_file:
        print(row)

#Read insurance.csv
early_congress = []
late_congress = []
import csv
import pandas as pd
import statistics
with open('bills.csv', 'r') as bill_file:
    fieldnames = ['bill_number', 'congress', 'bill_title', 'bill_subtitle']
    csv_reader = csv.DictReader(bill_file, delimiter = ',', skipinitialspace=True, 
                               fieldnames = fieldnames)
    for row in bill_file:
        if ['congress'] == '104th':
            early_congress.append('bill_subtitle', 'bill_number', 'congress')
            for row in early_congress:
                total_count = early_congress['bill_subtitle'].count
                print(total_count + 1)
