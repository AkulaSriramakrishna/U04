import mysql.connector
import pytest
my_db = None

def setup_module():
    my_db = mysql.connector.connect(
        host='localhost',
        user='root',
        password='rps@123',
        database='alims'
    )
    print('\n  db connection successfull')

def teardown_module():
    my_db.Close()
    print('\n Code for closing db connection')

def test_a1():
    print('\ntest case 1')

def test_a2():
    print('\ntest case 2')

def test_a3():
    print('\ntest case 3')