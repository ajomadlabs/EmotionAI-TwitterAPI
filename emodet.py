'''--------------------------------------------------------------------------
	Importing The Required Modules
--------------------------------------------------------------------------'''

import tweepy									#Importing the twitter module for connecting the API 
from textblob import TextBlob							#Importing the TextBlob module for the Sentimental Processing of the Text

'''-----------------------------------------------------------------------'''

'''--------------------------------------------------------------------------
	Twitter API Connection Keys
--------------------------------------------------------------------------'''

con_key = 'CkdvlxR7MZgzfWWX5QCV6L7hn'						#Consumer Key
con_sec = 'nfXie6Az8JQkp8LXLFJ9fM3GAigsNBAnqbo9a4tbnUXzhiKAQQ'			#Consumer Secret

acc_tok = '2699851880-Qc2GwAjEFXNHN1n25mW3K5eoRrP2tnHagPVoL2u'			#Access Token	
acc_sec_tok = '3cqzY9DC39vQtyeUmwiMocR9kbNxg948sCCdYqlSMQeFm'			#Access Token Secret

auth = tweepy.OAuthHandler(con_key, con_sec)					#Twitter authorisation handler is called for authorising the connection, giving conkey and consec
auth.set_access_token(acc_tok, acc_sec_tok)					#Setting the authorisation access to Twitter

'''-----------------------------------------------------------------------'''
	
'''--------------------------------------------------------------------------
	Connecting Twitter API
--------------------------------------------------------------------------'''
	
api = tweepy.API(auth)								#Twitter API authorisation, giving auth

'''-----------------------------------------------------------------------'''

'''--------------------------------------------------------------------------
	Searching The Particular Tweets About A Topic
--------------------------------------------------------------------------'''

pub_tweet = api.search('Dhoni')							#Twitter is searched for the given word

'''-----------------------------------------------------------------------'''

'''--------------------------------------------------------------------------
	Writing The Output To An External File
--------------------------------------------------------------------------'''
	
outfile2 = open('tweetanalys1.csv','w')						#File opened in write mode
for tweet in pub_tweet:								#A loop to go through all the tweets
	analys = TextBlob(tweet.text)						#Assiging the tweet to a varible in TextBlob
	if analys.sentiment.polarity >= 0:					#Analysing the sentiment polarity if > 0 then positive
		outfile2.write(str(analys) + "\n")				#Writing the particular tweet to the file 
		outfile2.write("Positive" + "\n")				#Writing the label corresponding the status
	elif analys.sentiment.polarity < 0:					#Analysing the sentiment polarity if < 0 then negative
		outfile2.write(str(analys) + "\n")				#Writing the particular tweet to the file
		outfile2.write("Negative" + "\n")				#Writing the label correspondingly
outfile2.close()								#CLosing the file

'''-----------------------------------------------------------------------''' 
