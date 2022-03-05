import snowflake.connector
import getpass

account = input('Snowflake account: ')
username = input('User name: ')
pword = getpass.getpass('Password: ')
defwh = username + '_WH'
defdb = username + '_DB'
defschema = 'PUBLIC'

# current = 'SnowPass@1$'

con = snowflake.connector.connect(
   user=username,
   password=pword,
   account=account,
   warehouse=defwh,
   database=defdb,
   schema=defschema
)
curs = con.cursor()
try:
   curs.execute("SELECT CURRENT_TIMESTAMP()")
   for (col1) in curs:
      print('{0}'.format(col1))
finally:
   curs.close()

curs = con.cursor()
try:
   curs.execute("SELECT * FROM PANDA_DB.PUBLIC.PEOPLE")
   for(col1, col2, col3) in curs:
      print('{0}, {1}, {2}'.format(col1, col2, col3))
finally:
   curs.close()

# import pandas as pd
# curs = con.cursor()
# try:
#    curs.execute("SELECT * FROM PANDA_DB.PUBLIC.PEOPLE")
#    dat = curs.fetchall()
#    peopleDF = pd.DataFrame(dat, columns=curs.description)
#    print(peopleDF.to_string())
# finally:
#    curs.close()
