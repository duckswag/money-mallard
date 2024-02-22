import os
from random import choice
global teamnames, abrvs, fullnames, cities
badtakes = [
  "Honestly, I think Victor Wembenyama has already passed up Shaq.",
  "Anyone else feel like Payton Pritchard would be an All-Star in 2015?",
  "The Detroit Pistons would beat the Bucks if they had Khris Middleton still.",
  "Seth isn't much worse than Steph rn.",
  "Moses Malone is a top 5 player ever.",
  "Wilt would average 65 in Jordan's era.",
  "Jusuf Nurkic is a top 10 center.",
  "Chris Paul is just as good as than Luka Doncic.",
  "Who says no? \n Milwakue Gets Chris Paul and a first \n Golden State gets Giannis Antetekumpo",
  "theswagduck is NOT cool (grass is blue)"
]
imgtab = [
  "lmao", "neutral", "yell", "huh"
]
teams = {
  "ATL": "Atlanta Hawks",
  "BOS": "Boston Celtics",
  "BKN": "Brooklyn Nets",
  "CHA": "Charlotte Hornets",
  "CHI": "Chicago Bulls",
  "CLE": "Cleveland Cavaliers",
  "DAL": "Dallas Mavericks",
  "DEN": "Denver Nuggets",
  "DET": "Detroit Pistons",
  "GSW": "Golden State Warriors",
  "HOU": "Houston Rockets",
  "IND": "Indiana Pacers",
  "LAC": "Los Angeles Clippers",
  "LAL": "Los Angeles Lakers",
  "MEM": "Memphis Grizzlies",
  "MIA": "Miami Heat",
  "MIL": "Milwaukee Bucks",
  "MIN": "Minnesota Timberwolves",
  "NOP": "New Orleans Pelicans",
  "NYK": "New York Knicks",
  "OKC": "Oklahoma City Thunder",
  "ORL": "Orlando Magic",
  "PHI": "Philadelphia 76ers",
  "PHX": "Phoenix Suns",
  "POR": "Portland Trail Blazers",
  "SAC": "Sacramento Kings",
  "SAS": "San Antonio Spurs",
  "TOR": "Toronto Raptors",
  "UTA": "Utah Jazz",
  "WAS": "Washington Wizards"
}
teamnames = '``` 76ers \n Bucks \n Bulls \n Cavaliers \n Celtics \n Clippers \n Grizzlies \n Hawks \n Heat \n Hornets \n Jazz \n Kings \n Knicks \n Lakers \n Magic \n Mavericks \n Nets \n Nuggets \n Pacers \n Pelicans \n Pistons \n Raptors \n Rockets \n Spurs \n Suns \n Thunder \n Timberwolves \n Trail Blazers \n Warriors \n Wizards```'
abrvs = '``` ATL \n BOS \n BKN \n CHA \n CHI \n CLE \n DAL \n DEN \n DET \n GSW \n HOU \n IND \n LAC \n LAL \n MEM \n MIA \n MIL \n MIN \n NOP \n NYK \n OKC \n ORL \n PHI \n PHX \n POR \n SAC \n SAS \n TOR \n UTA \n WAS```'
fullnames = '``` Atlanta Hawks \n Boston Celtics \n Brooklyn Nets \n Charlotte Hornets \n Chicago Bulls \n Cleveland Cavaliers \n Dallas Mavericks \n Denver Nuggets \n Detroit Pistons \n Golden State Warriors \n Houston Rockets \n Indiana Pacers \n Los Angeles Clippers \n Los Angeles Lakers \n Memphis Grizzlies \n Miami Heat \n Milwaukee Bucks \n Minnesota Timberwolves \n New Orleans Pelicans \n New York Knicks \n Oklahoma City Thunder \n Orlando Magic \n Philadelphia 76ers \n Phoenix Suns \n Portland Trail Blazers \n Sacramento Kings \n San Antonio Spurs \n Toronto Raptors \n Utah Jazz \n Washington Wizards```'
cities = '``` Atlanta \n Boston \n Brooklyn \n Charlotte \n Chicago \n Cleveland \n Dallas \n Denver \n Detroit \n Golden State \n Houston \n Indiana \n Los Angeles \n Memphis \n Miami \n Milwaukee \n Minnesota \n New Orleans \n New York \n Oklahoma City \n Orlando \n Philadelphia \n Phoenix \n Portland \n Sacramento \n San Antonio \n Toronto \n Utah \n Washington```'
def get_response(user_input: str, user) -> str:
  lowered: str = user_input.lower()
  if lowered.startswith("."):
    if lowered == ".".replace(".", ""):
      mnbvcxz = ""
    elif 'help' in lowered:
      return "help_embed"
    elif 'memes' in lowered:
      return "memes_embed"
    elif 'meme' in lowered and not 'memes' in lowered:
      otherchar: str = lowered[6:].lower()
      if otherchar not in imgtab:
        return "Sorry, " + '"' + otherchar + '"' + " isn't a valid meme name."
      else:
         return otherchar
    elif 'feedback' in lowered:
      charr: str = lowered[9:].lower()
      if charr == '':
        return "What is that? Chris Paul's ring collection? 😂😂 Please say more than nothing."
      else:
        return "feedback_ret" + charr
    elif 'vids' in lowered:
      characters: str = lowered[6:].lower()
      if characters == '':
        return "vids_embed"
      else:
        return "ytscr " + characters
    elif 'whowins' in lowered:
      characters: str = lowered[9:].lower()
      charmin = characters.replace(characters[3:], "").upper()
      charmin2 = characters[3:].upper()
      if charmin in teams and charmin2 in teams:
        selec = str(choice([teams.get(charmin), teams.get(charmin2)]))
        sel = choice(["I think the " + selec + " will win.", "The " + selec + " will win.", "The " + selec + "."])
        return sel
      elif len(charmin + charmin2) < 6:
        return "Sorry, I need at least two teams with 3 letter abbreviation to compare."
      elif charmin not in teams and charmin2 in teams and len(charmin + charmin2) >= 6:
        return "Sorry, " + charmin + ' is not a valid team. \n \n The proper formatting could be `.whowins ATLBOS` for example.'
      elif charmin2 not in teams and charmin in teams and len(charmin + charmin2) >= 6:
        return "Sorry, " + charmin2 + " is not a valid team. \n \n The proper formatting could be `.whowins ATLBOS` for example."
      else:
        return "Sorry, " + charmin + " and " + charmin2 + " are not valid teams. \n \n The proper formatting could be `.whowins ATLBOS` for example."
    elif 'teams' in lowered:
      if len(lowered[7:]) == 0:
        return "teams_embed"
      elif lowered[7:] in globals():
        return globals()[lowered[7:]]
      else:
        return "teams_embed"
    elif 'badtake' in lowered:
      return "badtake " + choice(badtakes)
    elif 'mytake' in lowered:
      return 'mytake'
    elif 'info' in lowered:
      return "info_embed"
    elif 'add' in lowered:
      invite = os.environ['InviteURL']
      return str(invite)
    else:
      return choice(['I dont understand what you are saying.', 
                     "Excuse me, I don't know what you mean.", "I don't understand that command."])
      
