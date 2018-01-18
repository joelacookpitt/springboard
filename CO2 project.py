
import pandas as pd
import numpy as np
""" copy pasted this dictionary in an attempt to create a new column in "coal" dataframe using following code:
    coal['StateAB']=us_state_abbrev.get(coal.State)
us_state_abbrev = {
    'Alabama': 'AL',
    'Alaska': 'AK',
    'Arizona': 'AZ',
    'Arkansas': 'AR',
    'California': 'CA',
    'Colorado': 'CO',
    'Connecticut': 'CT',
    'Delaware': 'DE',
    'Florida': 'FL',
    'Georgia': 'GA',
    'Hawaii': 'HI',
    'Idaho': 'ID',
    'Illinois': 'IL',
    'Indiana': 'IN',
    'Iowa': 'IA',
    'Kansas': 'KS',
    'Kentucky': 'KY',
    'Louisiana': 'LA',
    'Maine': 'ME',
    'Maryland': 'MD',
    'Massachusetts': 'MA',
    'Michigan': 'MI',
    'Minnesota': 'MN',
    'Mississippi': 'MS',
    'Missouri': 'MO',
    'Montana': 'MT',
    'Nebraska': 'NE',
    'Nevada': 'NV',
    'New Hampshire': 'NH',
    'New Jersey': 'NJ',
    'New Mexico': 'NM',
    'New York': 'NY',
    'North Carolina': 'NC',
    'North Dakota': 'ND',
    'Ohio': 'OH',
    'Oklahoma': 'OK',
    'Oregon': 'OR',
    'Pennsylvania': 'PA',
    'Rhode Island': 'RI',
    'South Carolina': 'SC',
    'South Dakota': 'SD',
    'Tennessee': 'TN',
    'Texas': 'TX',
    'Utah': 'UT',
    'Vermont': 'VT',
    'Virginia': 'VA',
    'Washington': 'WA',
    'West Virginia': 'WV',
    'Wisconsin': 'WI',
    'Wyoming': 'WY',
}
"""

""" Here's the state name to abbreviation package I tried and failed to import:
    pip install us
    import us
Here's the url that I got this from:
    https://pypi.python.org/pypi/us
"""

"""
df = pd.read_csv('..\Downloads\LUNG_DISEASE2015.csv',index_col='STATE')
df1 = df.iloc[:,[0]]
print(df1.head())
np2 = np.loadtxt('..\Downloads\Table_MF.txt',delimiter='\t',dtype=str)
df2 = pd.DataFrame(np2)
df3 = df2.iloc[:,[1,2]]
print(df3.head())
"""

coal=pd.read_excel('coal_table.xlsx','Table')
ng=pd.read_csv('natural_gas_table.csv')
coal.columns=['State','October 2017','October 2016']
print(coal.head())
print(coal.iloc[0][0])

