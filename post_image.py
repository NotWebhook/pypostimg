import tweepy


consumer_key = ".."
consumer_secret_key = "..."

access_token = ".."
access_token_secret = "..."

auth = tweepy.OAuthHandler(consumer_key, consumer_secret_key)
auth.set_access_token(access_token,access_token_secret)

api = tweepy.API(auth, wait_on_rate_limit=True)

def profile_image(filename):
    api.update_profile_image(filename)

def update_profile_info(name, url, location, description):
    api.update_profile(name, url, location, description)

def post_tweet(text):
    api.update_status(text)

def upload_media(text, filename):
    media = api.media_upload(filename)
    api.update_status(text, media_ids = [media.media_id_string])

upload_media("..", ".") 
print("Image posted!")
