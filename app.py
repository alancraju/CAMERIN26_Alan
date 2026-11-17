# import pymysql

# connection = pymysql.connect(
#     host = 'localhost',
#     user = 'python_app_slot2',
#     password = 'python@123',
#     database = 'camerin',
#     port = 3306
# )
# # print("MySql connection successfull")
# # print(connection.__dict__)

# try:
#     # cursor =connection.cursor()
#     with connection.cursor() as cursor:
#         # cursor.execute("SELECT * FROM students")
#         # records = cursor.fetchall(4)
#         # print(records)
#         # for record in records:
#         #     print(record)
#         query = f"""SELECT * 
#                 FROM students
#                 WHERE city = 'Kochi'"""
#         cursor.execute(query)
#         result=cursor.fetchall()
#         print(result)

#         username = ""
#         password = ""
#         query = f"""
#                 SELECT * FROM users
#                 WHERE username = %s    for sql injection is is used for protection of username and password
#                 AND password = %s
# """
#         cursor.execute(query,(username,password))    here it is protected in tuple
# except: #except Exception as e:
#     # print(f"Error : {e}")
#     print("Something Wrong")
# finally:
#     connection.close()
#     print("Operations Completed")



import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'python_app_slot2',
    password = 'python@123',
    database = 'camerin',
    port = 3306
)
# print("MySql connection successfull")
# print(connection.__dict__)

try:
    # cursor =connection.cursor()
    with connection.cursor() as cursor:
        # cursor.execute("SELECT * FROM students")
        # records = cursor.fetchall(4)
        # print(records)
        # for record in records:
        #     print(record)
        
        user_input = "' OR '1'='1"
        query = f"""SELECT * FROM students
        WHERE s_name='{user_input}'"""
    #    print(query)

        cursor.execute(query)
        print(cursor.fetchall())

#         username = ""
#         password = ""
#         query = f"""
#                 SELECT * FROM users
#                 WHERE username = %s
#                 AND password = %s
# """
        # cursor.execute(query,(username,password))

        query = """
           INSERT INTO students
           VALUES(%s,%s,%s,%s)
        """
        values = (108,"Akhil","akhil@gmail.com","Kochi")

        cursor.execute(query,values)
        connection.commit()
except Exception as e:
    print(f"Error : {e}")
finally:
    connection.close()
    print("Operations Completed")



# update,delete,truncate,drop    do it