import tweepy
import os
from dotenv import load_dotenv

# Load API keys
load_dotenv()
BEARER_TOKEN = os.getenv("TWITTER_BEARER_TOKEN")  # Use Bearer Token only

# Authenticate with Twitter API v2
client = tweepy.Client(bearer_token=BEARER_TOKEN)

def get_user_tweets_v2(username, count=5):
    """Fetch recent tweets from a specific user using Twitter API v2."""
    try:
        # Get user ID from username
        user = client.get_user(username=username, user_fields=["id"])
        if not user.data:
            print("User not found.")
            return

        user_id = user.data.id

        # Get tweets from user timeline
        tweets = client.get_users_tweets(id=user_id, max_results=count, tweet_fields=["created_at", "text"])

        if tweets.data:
            for tweet in tweets.data:
                print(f"[{tweet.created_at}] {username}: {tweet.text}\n")
        else:
            print("No recent tweets found.")
    
    except tweepy.TweepyException as e:
        print(f"Error fetching tweets: {e}")

# Example usage
if __name__ == "__main__":
    user = input("Enter Twitter username: ")
    get_user_tweets_v2(user, count=5)
