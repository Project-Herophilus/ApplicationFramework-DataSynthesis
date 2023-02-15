# This is a sample Python script.

# Articles
# Env
# https://able.bio/rhett/how-to-set-and-get-environment-variables-in-python--274rgt5
# https://www.nylas.com/blog/making-use-of-environment-variables-in-python/
# PostgreSQL Databases
# https://towardsdatascience.com/creating-a-python-postgresql-connection-for-absolute-beginners-501b97f73de1
# https://www.commandprompt.com/education/how-to-connect-to-postgresql-database-server-using-python/

# Packages
# pip install load_dotenv
# pip install psycopg2
# pip install python-decouple

# Press ⌃R to execute it or replace it with your code.
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import os
import psycopg2
from decouple import config

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press ⌘F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm App')
# See PyCharm help at https://www.jetbrains.com/help/pycharm/

# Get environment variables
#dbHostName = os.getenv('dbHost')
#dbPortNumber = os.environ.get('dbPort')
#dbUserName= os.environ.get('dbUser')
#dbPassword=os.environ.get('dbPassword')

# .env params
dbHostName = config('dbHost')
dbPortNumber = config('dbPort')
dbUserName= config('dbUser')
dbPassword= config('dbPassword')
dbName = config('dbName')

print('------------------')
print('Database Name:'+dbName)
print('Host:'+dbHostName)
print('Port: '+dbPortNumber)
print('User Name'+dbUserName)
print('Password'+dbPassword)
print('------------------')

# Connecting to PostgreSQL
conn = psycopg2.connect(
    #dbname=os.environ.get("POSTGRES_DB"),
    #user=os.environ.get("POSTGRES_USER"),
    #password=os.environ.get("POSTGRES_PASS"),
    #host=os.environ.get("POSTGRES_HOST"),
    #port=os.environ.get("POSTGRES_PORT")
    dbname = dbName,
    user = dbUserName,
    password = dbPassword,
    host = dbHostName,
    port = dbPortNumber
)

cursorObject = conn.cursor()
print(cursorObject.execute('SELECT * from refdata_status'))

#with conn.cursor() as cursor:
#    cursor.execute('SELECT VERSION()')
#    print(cursor.fetchone())
 #   print("connected")