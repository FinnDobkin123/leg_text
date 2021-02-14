#Import libraries
import pandas as pd
import csv
import statistics

#Read file in
url = 'https://github.com/FinnDobkin123/leg_text/blob/main/congress.csv'
congress_file = pd.read_csv(url, index_col = 0)
congress_df = pd.DataFrame(data = congress_file)
congress_df.head(5)

#Create list of 104th Congress
early_congress = []
late_congress = []
for congress in congress_file:
    if ['Congress'] == '104th':
        early_congress.append(str(row['Bill Title']))
    else:
        late_congress.append(str(row['Bill Title']))
