import tweepy
import time


auth = tweepy.OAuthHandler('VTc8jPrbGGb5LaoR122dlDabL','cSfUeFVe7UEr4P4IE5tRGSTMFVz03rVdSs3aUeCqWvyui23SJU')
auth.set_access_token('1316961768342646784-Zv3um7iuqpw8nOzucggffncZiBfPCJ', 'w9bOGljfHFvH6F2V3Tfhykcc9mE2fexs5EC3y5XF2AqIk')

api = tweepy.API(auth,wait_on_rate_limit=True,wait_on_rate_limit_notify=True)
user = api.me()

api = tweepy.API(auth)


#prints the follower of screen_name
def main():
    users = tweepy.Cursor(api.followers,screen_name="realdonaldtrump",count=10).items()
    for i in range(0,10):
        try:
            user = next(users)
            print(user.screen_name)
            print(user.name)
        except tweepy.TweepError:
            print("I it out of range pls wait.....")
            time.sleep(10)

main()

#genrs bot will help you to  follow back

def limit_handler(cursor):
    try:
        while True:
            yield cursor.next()
    except tweepy.RateLimitError:
        time.sleep(10)
    except tweepy.TweepError as er:
        print(er)
    except StopIteration:
        print("error")

search_string ="python" 
nooftweet =2

for tweet in tweepy.Cursor(api.search,search_string).items(nooftweet):
    try:
        tweet.favorite() # if ypu wanna retweet instead of fav then just tweet.retweet()
        print("I like this tweet!")
    except tweepy.TweepError as e:
        print(e)
    except StopIteration:
        break

for twet in tweepy.Cursor(api.search,search_string).items(nooftweet):
    try:
        twet.retweet() # if ypu wanna retweet instead of fav then just tweet.retweet()
        print("ok done!")
    except tweepy.TweepError as e:
        print(e)
    except StopIteration:
        break


for follower in tweepy.Cursor(api.followers).items():
    if follower.name == 'Charu Rakhade':
        follower.follow()






