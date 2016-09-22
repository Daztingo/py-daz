# coding=utf-8
import tweepy
import auth
import stream


authentificationToken = auth.initAuth()
api = auth.initApi(authentificationToken)

print(
"""########################################################

           Welcome to Twitter                         
           Please make à choice                       
           =============================	       
           1- Get last timeline statuses             
           2- get stream for given keyword
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
		stream.getStatuses(api)
	elif userChoice == '2' :
		stream.getStream(api, authentificationToken)




 
 

