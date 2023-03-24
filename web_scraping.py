import requests
import pandas as pd
from bs4 import BeautifulSoup

url = "https://one-versus-one.com/en/rankings/all/top-scorers"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

Players = []
for name in soup.find_all("div",class_="player-name"):
    Players.append(name.text)

Team = []
for teams in soup.find_all("span", class_="team-name"):
    Team.append(teams.text)

Goals = []
for goal in soup.find_all("td",class_="top-scorers__value" ):
    var = goal.text
    clean_var = var.replace(" ","").replace("\r\n", "")
    Goals.append(clean_var)

df = pd.DataFrame({'Players' : Players, 'Team': Team, 'Goals': Goals})
print(df)