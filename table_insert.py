import api_connect
import mysql.connector

# need to add data into separate columns
def TableInsert(_response):
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        database='db_air_api',
        username = "Arduino",
        password = "x0192288!"
        )

        print(mydb)
        mySql_insert_query = """INSERT INTO air_api (api_id,response) 
                            VALUES 
                            (%s, %s) """

        record = (None,_response)
        cursor = mydb.cursor()
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(cursor.rowcount, "Record inserted successfully into table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into table {}".format(error))

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

            print("MySQL connection is closed")

def TableInsertMultiple(tupleReceived):
    response = tupleReceived[0]
    city = tupleReceived[1]
    temperature = tupleReceived[2]
    insertTime=tupleReceived[3]
    date = tupleReceived[4]
    print(date)
    try:
        mydb = mysql.connector.connect(
        host="localhost",
        database='db_air_api',
        username = "Arduino",
        password = "x0192288!"
        )

        print(mydb)
        mySql_insert_query = """INSERT INTO air_api (api_id,response,city,temperature,insertTime,date) 
                            VALUES 
                            (%s, %s,%s,%s,%s,%s) """

        record = (None,response,city,temperature,insertTime,date)
        cursor = mydb.cursor()
        cursor.execute(mySql_insert_query, record)
        mydb.commit()
        print(cursor.rowcount, "Record inserted successfully into table")
        cursor.close()

    except mysql.connector.Error as error:
        print("Failed to insert record into table {}".format(error))

    finally:
        if mydb.is_connected():
            cursor.close()
            mydb.close()

            print("MySQL connection is closed")

#response = api_connect.GetDublin()
response = api_connect.parseDublin()
#print(response[0])

TableInsertMultiple(response)
