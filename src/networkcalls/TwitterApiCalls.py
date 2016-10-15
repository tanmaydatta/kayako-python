from src.authorization.AuthCredentials import AuthorizationCredentials
import tweepy

class TwitterApiCalls:
	def __init__(self):
		oauthCredentialObj = AuthorizationCredentials()
		self.connection = oauthCredentialObj.getConnection()

	def executeSearchApi(self, params):
		response = self.connection.search(q="#"+params["q"], max_id=params["max_id"], count="50")
		return response

