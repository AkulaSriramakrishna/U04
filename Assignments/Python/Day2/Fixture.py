import pytest
import mysql.connector
@pytest.fixture()
def input_a_value():
    mydb = mysql.connector.connect(
        host="localhost",
        user="root",
        password="rps@123",
        database='alims'
    )
    return mydb

def test_data(input_a_value):
    db=input_a_value
    cursor=db.cursor()
    cursor.execute("insert into login values ('Rahul','test@123')")
    db.commit()
    db.close()
