import tweepy
import webbrowser
import os 


def getQuote():

    filepath = 'quotes.txt'
    with open(filepath,encoding="utf8") as fp:
        quotes = fp.readlines()
        index = int(quotes[0])
        quote = quotes[index]
    
    newIndex = index+1
    
    newIndex = newIndex % len(quotes)
    
    quotes[0] = str(newIndex) + "\n"

    with open("quotes.txt", "w",encoding="utf8") as f:
        f.writelines(quotes)


    return quote

def Twitter_authenciate():
    # credentials to login to twitter api

    
    auth = tweepy.OAuthHandler('', '')
    auth.set_access_token('', '')
        
    api = tweepy.API(auth)


    return api

def tweet(quote,api):
    tweet = quote
    api.update_status(tweet)

if __name__ == "__main__":

    quote = getQuote()
    api = Twitter_authenciate()
    tweet(quote,api)
