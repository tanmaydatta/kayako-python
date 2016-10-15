import json
import ipdb

class Tweets:
	def extractRetweetedTweets(self, result):
		response = {}
		response["tweets"] = []
		response["status"] = "success"
		response["max_id"] = result.max_id

		for tweet in result:
			if tweet.retweet_count:
				response["tweets"].append({"text": tweet.text, "rc": tweet.retweet_count, "name": tweet.user.screen_name})

		return response

