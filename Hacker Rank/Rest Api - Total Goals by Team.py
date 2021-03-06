import requests

def getTotalGoals(team, year):
    link1 = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page=1"
    link2 = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page=1"

    data = requests.get(link1).json()
    pages = int(data['total_pages'])

    total = 0
    match = 0
    for i in range(1,pages+1):
        link = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team1={team}&page={i}"
        data = requests.get(link).json()
        data = data['data']
        for key in data:
            total+=int(key['team1goals'])
            match+=1
        

    data = requests.get(link2).json()
    pages = int(data['total_pages'])
    for i in range(1,pages+1):
        link = f"https://jsonmock.hackerrank.com/api/football_matches?year={year}&team2={team}&page={i}"
        data = requests.get(link).json()
        data = data['data']
        for key in data:
            total+=int(key['team2goals'])
    
    return total



team = input()
year = int(input())
res = getTotalGoals(team,year)
print(res)
