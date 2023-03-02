import pandas as pd
import time

# load data from a csv file using pandas (pd)
start_time = time.time()
df = pd.read_csv('MSFT.csv', encoding='utf8')
print(df)