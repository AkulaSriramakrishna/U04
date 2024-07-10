import pytest
import mysql.connector
import random

@pytest.fixture
def get_connection():
    my_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rps@123',
        database='alims'
    )
    return my_db

def test_create_record(get_connection):
    # perpared a random number for crating new table
    rdm = random.randint(10, 100)
    # table name is ready
    tablename = "test" + str(rdm)

    my_db = get_connection
    cursor = my_db.cursor()
    stmt = "create table " + tablename + ("(id int)")
    print("table created= ", tablename)
    cursor.execute(stmt)
    my_db.commit()

    try:
        stmt = 'select * from ' + tablename
    except:
        assert False, 'Can not create table'
    assert  True

    cursor.execute('drop table ' + tablename)
    my_db.commit()
    my_db.close()


def test_a1(get_connection):
    my_db=get_connection
    cursor=my_db.cursor()
    stmt = " select name from login  "
    result_set = cursor.execute(stmt)
    rslt = cursor.fetchall()
    my_db.commit()
    for temp in rslt:
        if "Akhil" in temp:
            assert True, 'User Found'
            break
        else:
            assert False, 'User not found'

def test_delete_user(get_connection):
    my_db = get_connection
    cursor = my_db.cursor()

    try:
        stmt = "delete  from login where name = 'Rahul' and password is not null"
        cursor.execute(stmt)
    except:
        assert False,'Unable to delete data'

    assert True,'Deleted successfully'


    my_db.commit()
    my_db.close()

def test_update_user(get_connection):
    my_db = get_connection
    cursor = my_db.cursor()

    try:
        stmt = " update login set password = 'Rahul@123'  where name = 'Rahul' and password is null "
        cursor.execute(stmt)
    except:
        assert False, 'Unable to update data'

    assert True, 'Updated successfully'

    my_db.commit()
    my_db.close()
