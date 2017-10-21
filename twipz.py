import tweepy
class Twipz:
    def __init__(self):
        self.__CONSUMER_KEY =''
        self.__CONSUMER_SECRET=''
        self.__access_key=""
        self.__access_secret=""
        self.__auth = tweepy.OAuthHandler(self.__CONSUMER_KEY,self.__CONSUMER_SECRET)
        self.__api=None
    def url(self):
        return self.__auth.get_authorization_url()
    def obtenerAccess(self,pin):
        x,y=self.__auth.get_access_token(pin)
        self.api=self.__auth
        self.access_key=x
        self.access_secret=y
    def asceso(self):
        self.__auth.set_access_token(self.access_key,self.access_secret)
        self.api=self.__auth

    @property
    def consumer_key(self):
        return self.__CONSUMER_KEY

    @property
    def consumer_secret(self):
        return self.__CONSUMER_SECRET

    @property
    def access_key(self):
        return self.__access_key
    @property
    def api(self):
        return self.__api
    @property
    def access_secret(self):
        return self.__access_secret

    @access_key.setter
    def access_key(self,val):
        self.__access_key=val

    @api.setter
    def api(self,val):
        self.__api=tweepy.API(val)

    @access_secret.setter
    def access_secret(self,val):
        self.__access_secret=val

    def visualizar(self,n):
        return self.api.home_timeline(count=n)
