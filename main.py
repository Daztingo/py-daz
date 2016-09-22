# coding=utf-8
import tweepy
import auth
import stream
import status


authentificationToken = auth.initAuth()
api = auth.initApi(authentificationToken)

print(
"""########################################################

           Welcome to Twitter                         
           Please make à choice                       
           =============================	       
           1- Get last timeline statuses             
           2- Get stream for given keyword
           3- Get last 20 tweets from given user
           Q- Quit	       
           
########################################################			
""")
		 
while 1 :
	userChoice = raw_input('Enter your choice ')
	userChoice = userChoice.lower()
	
	if userChoice == 'q' :
		exit('THE END')


	#Seems not to be beautiful, should search how to use dictionnary
	#But functions get differents arguments so that's the pb
	
	if userChoice == '1' :
		status.getStatuses(api)
	elif userChoice == '2' :
		stream.getStream(api, authentificationToken)
	elif userChoice =='3' :
		user = raw_input('Indicate user you want to look at : ')
		status.getStatusesForId(user, api)




 
 

