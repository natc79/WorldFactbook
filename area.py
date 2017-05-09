import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
query = 'SELECT SUM(area_land), SUM(area_water) FROM facts;'
sum_values = pd.read_sql_query(query,conn)
print(sum_values["SUM(area_land)"][0]/sum_values["SUM(area_water)"][0])
#print(sum_values["area_land"]/sum_values["area_water"])

#other things to investigate:
#1) Which countries lose population over next 35 years
#2) Which countries have lowest and highest population densities
#3) Which countries receive the most immigrants?  Which countries lose the most emigrants?
 