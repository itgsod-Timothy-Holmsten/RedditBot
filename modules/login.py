import requests
import json

class Login(object):
    def __init__(self, user):
        self.username = user.username
        self.password = user.password

        user_pass_dict = {'user': self.username,
                          'passwd': self.password,
                          'api_type': 'json'}

        user.client = requests.session()
        header = {'User-Agent' : 'Mozilla/5.0'}

        try:
            login = user.client.post('http://reddit.com/login', data=user_pass_dict, headers = header)


            print "User: %s, sucessfully logged in!" %self.username

            user.logged_in = True

        except():
            print Exception
