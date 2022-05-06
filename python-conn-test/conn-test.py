import snowflake.connector
import getpass

account = input('Snowflake account: ')
username = input('User name: ')
pword = getpass.getpass('Password: ')
defwh = f"{username}_WH"
defdb = f"{username}_DB"
defschema = "PUBLIC"

# current = 'SnowPass@1$'

con = snowflake.connector.connect(
   user=username,
   password=pword,
   account=account,
   warehouse=defwh,
   database=defdb,
   schema=defschema
)

# test the connection
curs = con.cursor()
try:
   curs.execute("SELECT CURRENT_TIMESTAMP()")
   for (col1) in curs:
      print('{0}'.format(col1))
finally:
   curs.close()

# run a basic query
curs = con.cursor()
query = f"SELECT * FROM {username}_DB.PUBLIC.PEOPLE"
try:
   curs.execute(query)
   for(col1, col2, col3) in curs:
      print('{0}, {1}, {2}'.format(col1, col2, col3))
finally:
   curs.close()

# pandas example with same query as above
import pandas as pd
curs = con.cursor()
query = f"SELECT * FROM {username}_DB.PUBLIC.PEOPLE"
try:
   curs.execute(query)
   dat = curs.fetchall()
   peopleDF = pd.DataFrame(dat, columns=curs.description)
   print(peopleDF.to_string())
finally:
   curs.close()

# TODO: add dunder main test and enclose code in def main()
