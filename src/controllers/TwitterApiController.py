from src.networkcalls.TwitterApiCalls import TwitterApiCalls
from src.models.Tweets import Tweets

class TwitterApiController:
	def __init__(self):
		self.tweet = Tweets()
		self.apiCall = TwitterApiCalls()

	def fetchTweet(self, params):
		final = {}
		try:
			result = self.apiCall.executeSearchApi(params)
			final = self.tweet.extractRetweetedTweets(result)
		except Exception as e:
			final["status"] = "failed"
			final["exception"] = str(e)

		return final
