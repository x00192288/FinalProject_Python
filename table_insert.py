import pyodbc
import api_connect

def TableInsertMultiple(tupleReceived):
    response = tupleReceived[0]
    response_string = response.decode('utf-8')

    city = tupleReceived[1]
    temperature = tupleReceived[2]
    insertTime = tupleReceived[3]
    date = tupleReceived[4]
    print(response)
    
    try:
        server = 'finalprojectx00192288.database.windows.net'
        database = 'FinalProject'
        username = 'ageraghty'
        password = 'x00192288!'
        driver = '{ODBC Driver 17 for SQL Server}'
        connection_string = f'DRIVER={driver};SERVER={server};DATABASE={database};UID={username};PWD={password}'

        mySql_insert_query = """INSERT INTO air_api (response, city, temperature, insertTime, date) 
                                VALUES 
                                (?, ?, ?, ?, ?)"""

        record = (response_string, city, temperature, insertTime, date)

        # Connect to the database
        connection = pyodbc.connect(connection_string)

        # Create a cursor
        cursor = connection.cursor()

        # Execute the INSERT query
        cursor.execute(mySql_insert_query, record)

        # Commit the transaction
        connection.commit()

        print(cursor.rowcount, "Record inserted successfully into table")

       
    except pyodbc.Error as error:
        print("Failed to insert record into table {}".format(error))

    finally:
    	if 'connection' in locals() and hasattr(connection, 'connected') and connection.connected:
            cursor.close()
            connection.close()
            print("ODBC connection is closed")
response = api_connect.parseDublin()
TableInsertMultiple(response)