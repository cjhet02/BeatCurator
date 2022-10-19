import requests
url = "https://scoresaber.com"
username = "Lorft" #just for testing, will be recieved through form
Params = {'search':username}
user = requests.get(url + "/api/players", params=Params)
res = user.json()
id = res['players'][0]['id']
lim = 10
Params = {'limit': lim+1}
scores = requests.get(url + "/api/player/" + id + "/scores", params=Params)
list = scores.json()
starSum = 0.00
for i in list['playerScores']:
    print("%s --- %d - %d pp" %(i['leaderboard']['songName'], i['score']['baseScore'], i['score']['pp']))
    starSum += i['leaderboard']['stars']

print("Average Star Rating: %d" %(starSum/lim))
