import pytest
import mysql.connector
@pytest.fixture()
def input_value():
    input = 9
    return input

@pytest.fixture()
def db_connection():
    my_db = mysql.connector.connect(
        host='localhost',
        user ='root',
        password = 'rps@123',
        database ='alims'
    )
    return  my_db