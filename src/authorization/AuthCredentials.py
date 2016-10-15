import tweepy

class AuthorizationCredentials:
    def __init__(self):
        self.token = {}
        self.token['consumer_key'] = "fyi65m30QRabcDv3fJXHGcIdk";
        self.token['consumer_key_secret'] = "8eJ09L2p8oEfnUW9gpFkK0z6b1PaIDfoLmhZJCR5OV06kfsvKl";
        self.token['access_token'] = "82867644-GqPOJynbyfgc451HjNwn5QWvV6KsU5tCvbxvuqwaM";
        self.token['access_token_secret'] = "oalNtrqjgbowcwohhSpCc59WK2EmAEgMEmvAvU4Krg0g7";
        self.auth = tweepy.OAuthHandler(self.token['consumer_key'], self.token["consumer_key_secret"])
        self.auth.set_access_token(self.token['access_token'], self.token['access_token_secret'])
        self.api = tweepy.API(self.auth)

    def getConnection(self):
        return self.api
