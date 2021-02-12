import config
from instapy import InstaPy

#login session
session = InstaPy(username=config.username,
                  password=config.password,
                  headless_browser=True)
session.login()

#This line will like 10 posts in the #tags you have listed
session.like_by_tags(["10over10",
                      "gainwithmchina",
                      "gainwiththeepluto"], amount=10)

#Am making it 50 because if you follow a lot IG may terminate you
#This line will follow the owners of the photos you like 
session.set_do_follow(True, percentage=50)

session.set_do_comment(True, percentage=50)
session.set_comments(["Legit",
                      "Epic Staff"]) 
#To put an emoji... start with u"nice .."

session.end()


#RCS was here