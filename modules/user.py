from BeautifulSoup import BeautifulSoup

class User(object):
    def __init__(self, username, password):
        self.username = username
        self.password = password

        self.logged_in = False

        self.client = None #Used for handling cookies

    def karma(self):
        if self.logged_in:
            html = self.client.get('https://www.reddit.com/user/timsbot/submitted/').text

            soup = BeautifulSoup(html)

            #Find karma
            k = soup.find('span', {'class': 'karma'}).text

            return k

