class Config(object):
    url = 'https://candymapper.com/'
    username = 'akulaakhil2808@gmail.com'
    password = 'Testing@123'
    username1 = 'akulaakhil2808@gmail.com'
    password1 = 'Testing@12'

class Registration(object):
    first_name = 'Anna'
    last_name = 'Singh'
    email = 'testing123@gmail.com'
    email1 = 'akulaakhil2808@gmail.com'
    phone_no = '123456789'
    message = 'This is a testing message'

class SuccessUrl(object):
    login_pass = 'https://candymapper.com/m/account', 'Login failed'
    login_failed = 'https://candymapper.com/m/login?err=FAILED_CONTACT_LOGIN&r=%2Fm%2Faccount&app=website'