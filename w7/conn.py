import psycopg2

conn = None

try:
    #Connection to database

    conn = psycopg2.connect(database="flis",user="postgres",password="xhdjxx9jq2051",host="127.0.0.1",port="5432")
    print("Database Connected")
    print(conn)


except (Exception, psycopg2.DatabaseError) as error:
    print(error)


finally:
    if conn is not None:
        conn.close() #close connection