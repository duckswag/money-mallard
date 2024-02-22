from urllib.request import urlopen 
import json 

def gettitle(vid):
  url = "https://www.youtube.com/oembed?url=http://www.youtube.com/watch?v=" + vid + "&format=json"
  response = urlopen(url) 
  data_json = json.loads(response.read()) 
  return data_json['title']
