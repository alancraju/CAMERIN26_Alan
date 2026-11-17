import pymysql

connection = pymysql.connect(
    host = 'localhost',
    user = 'python_app_slot2',
    password = 'python@123',
    database = 'camerin',
    port = 3306
)

try:
    with connection.cursor() as cursor:
#         query="""
#               ALTER TABLE students
#               MODIFY phone INT DEFAULT 1111111111;
# """
        # query= """
        #     ALTER TABLE students
        #     RENAME COLUMN phone TO contact_number
        # """
        query = """
              ALTER TABLE students
              DROP COLUMN contact_number
"""
        cursor.execute(query)
        connection.commit()
        print("Column created successfully...")
        query = "DESC students"
        cursor.execute(query)

        result=cursor.fetchall()
        for col in result:
            print(col)

except Exception as e:
    print(f"Error : {e}")
finally:
    connection.close()
    print("Operations Completed")
