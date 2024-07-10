import requests
import pytest


def test_list_user():
    res = requests.get('https://reqres.in/api/users?page=2')
    print( res.status_code)
    assert res.status_code == 200, 'List user does not exists'


def test_single_user():
    res = requests.get('https://reqres.in/api/unknown/2')
    print(res.status_code)
    assert res.status_code == 200, 'List user does not exists'

def test_single_user_Not_found():
    res = requests.get('https://reqres.in/api/users/23')
    print(res.status_code)
    assert res.status_code == 404, 'List user  exists'

def test_user_delete():
    res = requests.delete('https://reqres.in/api/users/2')
    print(res.status_code)
    assert res.status_code == 204, 'Unable to delete'

def test_user_list():
    res = requests.get('https://reqres.in/api/unknown')
    print(res.status_code)
    assert res.status_code == 200, 'Unable to delete'

def test_single_resource_not_Found():
    res = requests.get('https://reqres.in/api/unknown/23')
    print(res.status_code)
    assert res.status_code == 404, 'Resource not found'

def test_single_resource():
    res = requests.get('https://reqres.in/api/unknown/2')
    print(res.status_code)
    assert res.status_code == 200, 'Resource found'

def test_update_user():
    data = {
         "name": "morpheus",
         "job": "zion resident"
    }
    res = requests.put('https://reqres.in/api/users/2',data=data)
    print(res.status_code)
    assert res.status_code == 200, 'Unable to Update'

def test_update_user():
    data = {
         "name": "morpheus",
         "job": "zion resident"
    }
    res = requests.patch('https://reqres.in/api/users/2',data=data)
    print(res.status_code)
    assert res.status_code == 200, 'Unable to Update'
def test_create_user():
    data = {
        "name": "morpheus",
        "job": "leader"
    }
    res = requests.post('https://reqres.in/api/users', data=data)
    print(res.status_code)
    assert res.status_code == 201, 'Unable to create '

def test_delayed():
    data = {
    }
    res = requests.get('https://reqres.in/api/users?delay=3', data=data)
    print(res.status_code)
    assert res.status_code == 200, 'Unable to create '

def test_login():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "cityslicka"
    }
    res = requests.post('https://reqres.in/api/login', data=data)
    print(res.status_code)
    assert res.status_code == 200, 'Unable to login '

def test_login_unsuccessfull():
    data = {
    }
    res = requests.post('https://reqres.in/api/login', data=data)
    print(res.status_code)
    assert res.status_code == 400, 'Unable to login '

def test_register():
    data = {
        "email": "eve.holt@reqres.in",
        "password": "pistol"
    }
    res = requests.post('https://reqres.in/api/register', data=data)
    print(res.status_code)
    assert res.status_code == 200, 'Unable to register '

def test_register_unsuccessfull():
    data = {
        "email": "sydney@fife"
    }
    res = requests.post('https://reqres.in/api/register', data=data)
    print(res.status_code)
    assert res.status_code == 400, 'Unable to register '