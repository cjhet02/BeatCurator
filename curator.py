import requests
#get user's preferences with no wait
user = input("Enter Scoresaber profile url: ")
lim = input("Enter number of scores to consider: ")
#starRange = input("")
starBound = 0.5

#parse user id from url
id = ""
for i in reversed(range(len(user))) :
    if user[i] == '/':
        break
    id = user[i] + id


Params = {'limit': lim}
scores = requests.get("https://scoresaber.com/api/player/" + id + "/scores", params=Params)
list = scores.json()
starSum = 0.00
for i in list['playerScores']:
    print("%s - %.2f --- #%d - %d pp" %(i['leaderboard']['songName'], i['leaderboard']['stars'], i['score']['rank'], i['score']['pp']))
    starSum += i['leaderboard']['stars']

avStar = starSum/float(lim)
print("\nAverage Star Rating: %.2f" %(avStar))

Params = {
    'ranked': True,
    'minStar': avStar - starBound,
    'maxStar': avStar + starBound,
    'category': 2 #sorting by scores set (aka popularity)
}
songs = requests.get("https://scoresaber.com/api/leaderboards/", params=Params)
list = songs.json()
print("Your Recommendations:\n")
for i in list['leaderboards']:
    print("%s - %s --- %.2f " %(i['songName'], i['levelAuthorName'], i['stars']))