import psycopg2


try:

    rowList = list()

    conn = psycopg2.connect(
        host="localhost",
        database="dverental",
        user="postgresUser",
        password="postgresPW1")

    cur = conn.cursor()
    
    cur.execute('SELECT * from customer where customer_id <= 10')

    rows = cur.rowcount
    print ("Found " + str(rows) + " rows")


    ctr = 1

    rowList = cur.fetchall()

    #while ctr <= rows :
     #   full_record = cur.fetchone()
      #  print ("record number ..." + str(ctr))
        #rowList.append(full_record)
       # ctr = ctr +1
    
    print ("now going to print")

    #print (rowList)

    for record in rowList :
         print (record)

    cur.close()
except (Exception, psycopg2.DatabaseError) as error:
    print(error)

finally:
        if conn is not None:
            conn.close()
            print('Database connection closed.')

