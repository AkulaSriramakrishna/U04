import mysql.connector

def test_1(input_value):
    assert input_value == 5,'failed'

def test_2(input_value):
    assert input_value == 9,'failed'

def test_conn(db_connection):
    cursor = db_connection.cursor()
    stmt = "select name from login"
    result_set = cursor.execute(stmt)
    result = cursor.fetchall()
    for temp in result:
        if 'Akhil' in temp:
            assert True, 'User not found'
            print("\n user found")
            break
        else:
            assert False, 'User not found'


