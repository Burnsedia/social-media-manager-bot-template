import os
import requests
import tweepy
import openai
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# OpenAI API Key
openai.api_key = os.getenv("OPENAI_API_KEY")

# Instagram Credentials
IG_ACCESS_TOKEN = os.getenv("IG_ACCESS_TOKEN")
IG_BUSINESS_ID = os.getenv("IG_BUSINESS_ID")  # Must be the Business Account ID

# Twitter Credentials
TWITTER_BEARER = os.getenv("TWITTER_BEARER_TOKEN")
TWITTER_API_KEY = os.getenv("TWITTER_API_KEY")
TWITTER_API_SECRET = os.getenv("TWITTER_API_SECRET")
TWITTER_ACCESS_TOKEN = os.getenv("TWITTER_ACCESS_TOKEN")
TWITTER_ACCESS_SECRET = os.getenv("TWITTER_ACCESS_SECRET")

# Authenticate Twitter API v2
client = tweepy.Client(
    bearer_token=TWITTER_BEARER,
    consumer_key=TWITTER_API_KEY,
    consumer_secret=TWITTER_API_SECRET,
    access_token=TWITTER_ACCESS_TOKEN,
    access_token_secret=TWITTER_ACCESS_SECRET
)

# Authenticate Twitter API v1 for media uploads
auth = tweepy.OAuth1UserHandler(
    TWITTER_API_KEY, TWITTER_API_SECRET,
    TWITTER_ACCESS_TOKEN, TWITTER_ACCESS_SECRET
)
api = tweepy.API(auth)

# Generate Custom Messages with GPT
def generate_custom_message(username, base_message):
    prompt = f"Write a friendly Twitter DM to {username}. Include this call to action: '{base_message}'. Keep it short and professional."
    response = openai.Completion.create(model="gpt-4", prompt=prompt, max_tokens=50)
    return response.choices[0].text.strip()

# Post Image to Instagram
def post_to_instagram(image_url, caption):
    print("Posting to Instagram...")

    create_url = f"https://graph.facebook.com/v22.0/{IG_BUSINESS_ID}/media"
    publish_url = f"https://graph.facebook.com/v22.0/{IG_BUSINESS_ID}/media_publish"

    # Step 1: Create Media Object
    payload = {"image_url": image_url, "caption": caption, "access_token": IG_ACCESS_TOKEN}
    response = requests.post(create_url, data=payload)
    response_json = response.json()

    if "id" not in response_json:
        print("Error creating media container:", response_json)
        return

    media_id = response_json["id"]

    # Step 2: Publish Media
    publish_response = requests.post(publish_url, data={"creation_id": media_id, "access_token": IG_ACCESS_TOKEN})

    print("Instagram Post Published:", publish_response.json())

# Post Image to Twitter
def post_to_twitter(image_path, caption):
    print("Posting to Twitter...")

    try:
        # Upload media first
        media = api.media_upload(image_path)

        # Post tweet with media
        client.create_tweet(text=caption, media_ids=[media.media_id])

        print("Tweet Posted!")
    except Exception as e:
        print("Error posting to Twitter:", str(e))

# Send DMs to Twitter Followers
def dm_twitter_followers(base_message):
    try:
        followers = client.get_users_followers(id=client.get_me().data['id'])
        for follower in followers.data:
            custom_message = generate_custom_message(follower.username, base_message)
            client.create_direct_message(recipient_id=follower.id, text=custom_message)
            print(f"DM sent to {follower.username}")
    except Exception as e:
        print("Error sending DMs:", str(e))

# Main Workflow
if __name__ == "__main__":
    IMAGE_URL = "https://baileyburnsed.dev/CyberPunkLogo2.jpg"
    IMAGE_PATH = "CyberPunkLogo2.jpg"  # Ensure this file exists locally
    CAPTION = "Check out my latest CyberPunk Logo! #design #cyberpunk"
    SALES_SCRIPT = "Hey {username}, I noticed you're into cyberpunk aesthetics! Check out my latest work."

    # Post to Instagram
    # post_to_instagram(IMAGE_URL, CAPTION)

    # Post to Twitter
    post_to_twitter(IMAGE_PATH, CAPTION)

    # DM Twitter Followers
    dm_twitter_followers(SALES_SCRIPT)

