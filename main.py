import twitter;

api = twitter.Api(consumer_key='vLOImLTkAfh20n61M7QNuPDzL',
                  consumer_secret='R96EhFIExKUlHNsXxjBq88jhkvXzPMscNR7S1filRg7IZacjjC',
                  access_token_key='2745774121-mEljXbbrsOpXd2uSJFHaeRnPgrNtFP7jqv6gpcr',
                  access_token_secret='wRzznLRVjB9CyNXsrEes8Kvx56kxLN1qc3iNeyH7hx2er')
                      
print(api.VerifyCredentials())

statuses = api.GetUserTimeline(screen_name='dazleria')
print([s.text for s in statuses])

followers = api.GetFollowers('7374782')
print(followers)
