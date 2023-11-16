> Simple [Telegram Bot](https://core.telegram.org/bots "Telegram Bots") to Upload videos to [Youtube](https://youtube.com "YouTube") written in Python3.

## Contents

- [Info](#info)
- [Libraries Used](#libraries-used)
- [Setup](#setup)
- [Development Status](#development-status)
- [Screenshots](#screenshots)
- [Contact](#contact)
- [Commands](#commands)
- [Authors](#authors)
- [License](#license)

## Info

#### Project Update

This project was initially created by **[Christy Roys](https://github.com/odysseusmax/)**. I have recently modified the code, incorporating additional functions, commands, and ensuring compatibility with the latest versions of libraries.

#### Project Overview

The project involves the development of a Telegram bot utilizing the [Youtube Data API v3](https://developers.google.com/youtube/v3/ "Youtube Data API v3"). The primary purpose of the bot is to facilitate the seamless uploading of videos to YouTube.

For more details about the original project, you can refer to the [GitHub repository](https://github.com/odysseusmax/utube).

---

_Note: The modifications made to the code aim to enhance its functionality and ensure compatibility with the most recent library versions._

### Libraries Used

- [![Pyrogram](https://img.shields.io/badge/Pyrogram-latest-green?style=flat)](https://github.com/pyrogram/pyrogram "Pyrogram")
- [![Google Client API](https://img.shields.io/badge/Google%20Client%20API-latest-blue?style=flat)](https://github.com/googleapis/google-api-python-client "Google Client API")

## Setup

**⚠️Note: This project requires Python3.6 or higher**

#### Clone and setup virtual environment

**STEP : 1** Clone the git repository with Runing :

```git
git clone https://github.com/alpha-alexxx/YoutubeUploader
```

**STEP : 2** Go to the repository directory.

```bash
cd YoutubeUploader
```

---

_Now set Environment Variables in root folder with .env file._

**STEP : 3** Create environment file to save environments.

```
cp .env.sample .env
```

Add the following lines to it, replacing `API_ID`, `API_HASH`, `BOT_TOKEN`,`CLIENT_ID`,`CLIENT_SECRET`,`BOT_OWNER`,`AUTH_USERS`,`UPLOAD_MODE` &amp; `VIDEO_CATEGORY`;

**.env File Example:**

```
BOT_TOKEN="YOUR_BOT_TOKEN_HERE"
SESSION_NAME="your_session_name_here"
API_ID="your_api_id_here"
API_HASH="your_api_hash_here"
CLIENT_ID="your_client_id_here"
CLIENT_SECRET="your_client_secret_here"
BOT_OWNER="your_bot_owner_user_id_here"
AUTH_USERS="comma_separated_list_of_user_ids"
VIDEO_DESCRIPTION="This video is uploaded from telegram bot (example)"
VIDEO_CATEGORY="your_video_category_id_here(specific if you needed)"
UPLOAD_MODE="your_upload_mode_here"
```

### Environment Variables

- `BOT_TOKEN`(Required) - Get your bot token from [Bot Father](https://tx.me/BotFather "Bot Father").
- `SESSION_NAME`(optional) - Your bot's username.
- `API_ID`(Required) - Your telegram api id, get from [Manage Apps](https://my.telegram.org).
- `API_HASH`(Required) - Your telegram api hash, get from [Manage Apps](https://my.telegram.org).
- `CLIENT_ID`(Required) - Your google client id.
- `CLIENT_SECRET`(Required) - Your google client secret.
- `BOT_OWNER`(Required) - Telegram id of bot owner.
- `AUTH_USERS`(optional) - Telegram id's of authorised users, separated by `,`.
- `VIDEO_DESCRIPTION`(optional) - Any default description to be aded to the video.
- `VIDEO_CATEGORY`(optional) - YouTube's video category id. If not specified or specified id is invalid, category id will be selected randomly.
- `VIDEO_TITLE_PREFIX`(optional) - Any prefix to be added to the video's title.
- `VIDEO_TITLE_SUFFIX`(optional) - Any suffix to be added to the video's title.
- `UPLOAD_MODE`(optional) - The video's privacy status. Valid values for this property are: `private`, `public`, `unlisted`.
- `DEBUG` (optional) - Whether to set logging level to DEBUG. If set logging will be set to DEBUG level, else INFO level.

**Getting your `CLIENT_ID` and `CLIENT_SECRET`**

- Head to [Google console](https://console.developers.google.com "Google console"), create a new project named `Youtube Uploader` and enable `API'S AND SERVISES`. Search for `YOUTUBE DATA API v3` and enable the API. Go to [Credentials](https://console.developers.google.com/apis/credentials "Credentials") page, select your project `Youtube Uploader` create a new credential with `desktop` as type. Copy the `CLIENT_ID` and `CLIENT_SECRET`.
- You have to verify your application with google, only then you can make the uploaded videos public. YouTube changed its developer policy, and videos uploaded using unverfied applications will be kept private.

---

**Step : 4** Install requirements with running below command:

```
pip3 install -r requirements.txt
```

**Step : 5** **Run bot**

Lets run our bot for the first time!

```python3
 python3 -m bot
```

Certainly! Here's a more professional version:

Upon successful completion of the setup, the bot should be operational. Execute the `/start` command to verify the bot's live status. Follow the instructions provided by the bot to establish authorization and commence the uploading process.

### Development Status

[![Active](https://img.shields.io/badge/Status-Active-success?style=for-the-badge)](https://github.com/alpha-alexxx/YoutubeUploader)

🚀 **Active Development:** I am currently actively working on this project, implementing new features, fixing issues, and making continuous improvements. Your contributions and feedback are always welcome!

### Special notes

- With the Youtube Data API you are awarded with 10,000 points of requests. For one video upload it costs 1605 points, regardless of file size, which calculates to about 6 uploads daily. Once you have exhausted your daily points, you have to wait till daily reset. Resets happens at 0:00 PST, i.e. 12:30 IST. So make your uploads count.

- Uploading copyright contents will leads to immediate blocking of the video.

- By default, all the videos are uploaded as private with random category id unless you provide `UPLOAD_MODE` and `VIDEO_CATEGORY`. You may change it after youtube processes the video.

### Screenshots

<p align="center">

<img  width="25%" height="25%" src="./ss/overview.jpg">

<img  width="25%" height="25%" src="./ss/bot-start.jpg">

<img  width="25%" height="25%" src="./ss/bot-help.jpg">

<img  width="25%" height="25%" src="./ss/bot-authorise.jpg">

<img  width="25%" height="25%" alt="Upload" src="./ss/bot-upload.jpg">

</p>

### Contact


<a href="https://telegram.dog/LethargicBots"><img src="https://img.shields.io/badge/Telegram-Join%20Telegram%20Group-blue.svg?logo=telegram"></a>

### Commands

Edit the bot in [**BotFather**](https://t.me/BotFather) with command `/help` ⮞ `/mybots` ⮞ choose your bot by the username ⮞ click on Edit bot ⮞ click on edit commands ⮞ copy the below code and paste there and save it.

```
start -  Start the bot.
login - Log in to the bot
upload -  Initiate the upload process of video
help -  Get assistance or command information
logout - Log out from the bot
refresh -  Refresh or update auth token
```

### Authors
- Creator - ![Christy Roys](https://images.weserv.nl/?url=avatars.githubusercontent.com/u/35767464?v=4&h=32&w=32&fit=cover&mask=circle&maxage=7d) - [Christy Roys](https://github.com/odysseusmax/)
- Contributor - ![Ankit Kumar](https://images.weserv.nl/?url=avatars.githubusercontent.com/u/65218056?v=4&h=32&w=32&fit=cover&mask=circle&maxage=7d) - [Ankit Kumar](https://github.com/alpha-alexxx/)


### Follow Me: 
[![GitHub followers](https://img.shields.io/github/followers/alpha-alexxx?label=Follow&style=social)](https://github.com/alpha-alexxx/)

<p align='center'> <img src ='https://github-readme-stats.vercel.app/api?username=alpha-alexxx&show_icons=true&title_color=ffffff&icon_color=34abeb&text_color=daf7dc&bg_color=151515'/></p>

### License

Code released under [GNU General Public License v3.0](LICENSE).

[![License](https://img.shields.io/badge/License-GPL%20v3.0-blue.svg)](https://opensource.org/licenses/GPL-3.0)
