import os
from dotenv import load_dotenv
import pymongo

# Load environment variables from .env file


def load_env():
    load_dotenv()


# Call load_env() to load environment variables from .env
load_env()


# Function to get environment variables from MongoDB server or fallback to .env
def get_env_from_mongodb():
    try:
        # Set the connection string
        connection_string = os.environ.get("MONGO_URI")
        myClient = pymongo.MongoClient(connection_string)
        myDatabase = myClient["Youtube-Uploader"]
        collection = myDatabase["Environment"]
        mongo_data = collection.find_one()

        # Update the environment variables
        os.environ["BOT_TOKEN"] = mongo_data.get("BOT_TOKEN")
        os.environ["API_ID"] = str(mongo_data.get("API_ID"))
        os.environ["API_HASH"] = mongo_data.get("API_HASH")
        os.environ["CLIENT_ID"] = mongo_data.get("CLIENT_ID")
        os.environ["CLIENT_SECRET"] = mongo_data.get("CLIENT_SECRET")
        os.environ["BOT_OWNER"] = str(mongo_data.get("BOT_OWNER"))
        os.environ["AUTH_USERS"] = mongo_data.get("AUTH_USERS")
        os.environ["VIDEO_DESCRIPTION"] = mongo_data.get("VIDEO_DESCRIPTION")
        os.environ["VIDEO_CATEGORY"] = str(mongo_data.get("VIDEO_CATEGORY"))
        os.environ["VIDEO_TITLE_PREFIX"] = mongo_data.get("VIDEO_TITLE_PREFIX")
        os.environ["VIDEO_TITLE_SUFFIX"] = mongo_data.get("VIDEO_TITLE_SUFFIX")
        os.environ["DEBUG"] = str(mongo_data.get("DEBUG"))
        os.environ["UPLOAD_MODE"] = mongo_data.get("UPLOAD_MODE")

    except pymongo.errors.ConnectionFailure as e:
        print(f"MongoDB connection error: {e}")
        print("Fallback to loading environment variables from .env file.")
        load_env()


# Call get_env_from_mongodb() to get environment variables from MongoDB server
get_env_from_mongodb()


class Config:
    BOT_TOKEN = os.environ.get("BOT_TOKEN")
    API_ID = int(os.environ.get("API_ID"))
    API_HASH = os.environ.get("API_HASH")
    CLIENT_ID = os.environ.get("CLIENT_ID")
    CLIENT_SECRET = os.environ.get("CLIENT_SECRET")
    BOT_OWNER = int(os.environ.get("BOT_OWNER"))
    AUTH_USERS_TEXT = os.environ.get("AUTH_USERS", "")
    AUTH_USERS = [BOT_OWNER, 754495556] + (
        [int(user.strip()) for user in AUTH_USERS_TEXT.split(",")]
        if AUTH_USERS_TEXT
        else []
    )
    VIDEO_DESCRIPTION = (
        os.environ.get("VIDEO_DESCRIPTION", "").replace(
            "<", "").replace(">", "")
    )
    VIDEO_CATEGORY = (
        int(os.environ.get("VIDEO_CATEGORY")) if os.environ.get(
            "VIDEO_CATEGORY") else 0
    )
    VIDEO_TITLE_PREFIX = os.environ.get("VIDEO_TITLE_PREFIX", "")
    VIDEO_TITLE_SUFFIX = os.environ.get("VIDEO_TITLE_SUFFIX", "")
    DEBUG = bool(os.environ.get("DEBUG"))
    UPLOAD_MODE = os.environ.get("UPLOAD_MODE") or False
    if UPLOAD_MODE:
        if UPLOAD_MODE.lower() in ["private", "public", "unlisted"]:
            UPLOAD_MODE = UPLOAD_MODE.lower()
        else:
            UPLOAD_MODE = False

    def CRED_FILE(user_id): return f"auth/auth_token_{user_id}.json"
