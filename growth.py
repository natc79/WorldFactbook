import sqlite3
import pandas as pd
import math
conn = sqlite3.connect('factbook.db')

c = conn.cursor()
query = 'SELECT * FROM facts;'
facts = pd.read_sql_query(query,conn)
clean_facts = facts[facts["area_land"] != 0]

print(facts.shape, clean_facts.shape)

def final_pop(initpop,popgrw_rate):
    years = 2050-2015
    return( initpop*math.e**((popgrw_rate/100)*years) )

#use apply to compute what the data will be like for each row in the data
facts["population_2050"] = facts.apply(lambda x: final_pop(x["population"], x["population_growth"]), axis=1)

#now print out the countries with highest population in 2050
sort_pop_2050 = facts.sort_values("population_2050",axis=0, ascending=False)
print(sort_pop_2050["name"].head(10))




