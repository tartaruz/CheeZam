import mysql.connector as mysql
import atexit
class DbConnector:
    
    def __init__(self,
            HOST="sql31.mcb.webhuset.no",
            DATABASE="90567_schitzam",
            USER="90567_schitzam",
            PASSWORD="PREBOBU53"):
        # Connect to the database
        try:
            self.db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=3306)
        except Exception as e:
            print("ERROR: Failed to connect to db:", e)

        # Get the db cursor
        self.cursor = self.db_connection.cursor()

        print("Connected to:", self.db_connection.get_server_info())
        # get database information
        self.cursor.execute("select database();")
        database_name = self.cursor.fetchone()
        print("You are connected to the database:", database_name)
        print("-----------------------------------------------\n")
        atexit.register(self.goodbye)


    def close_connection(self):
        # close the cursor
        self.cursor.close()
        # close the DB connection
        self.db_connection.close()


    def open_connection(self,
            HOST="sql31.mcb.webhuset.no",
            DATABASE="90567_schitzam",
            USER="90567_schitzam",
            PASSWORD="PREBOBU53"):
        try:
            self.db_connection = mysql.connect(host=HOST, database=DATABASE, user=USER, password=PASSWORD, port=3306)
        except Exception as e:
            print("ERROR: Failed to connect to db:", e)
        # Get the db cursor
        self.cursor = self.db_connection.cursor()
        self.cursor.execute("select database();")
        database_name = self.cursor.fetchone()

    def goodbye(self):
        self.close_connection()
        print('Goodbye,it was nice to meet you.')



