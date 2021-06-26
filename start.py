from instagrapi import Client
from instagrapi.types import StoryLink
import config

#Read user information from config
ID = config.userID
PW = config.userPW

#Login Processing
cl = Client()
cl.login(ID, PW)
#cl.login(ID, PW, verification_code="<2FA CODE HERE>") 2FA support
#cl.loginby_sessionid("token") use this for token login
print("login success!")
print(cl.user_info(cl.user_id))

#video to post
media_path = cl.video_download(
    cl.media_pk_from_url('https://www.instagram.com/p/CQlmi47j5ai/')
)

#upload a video to a story
cl.video_upload_to_story(
    media_path, #specifying a video here
    "from instagrapi",
    links=[StoryLink(webUri='https://meru-golang.dev')], #specify a story link
)
print("upload success!")