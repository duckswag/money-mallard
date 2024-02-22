import os
import requests

url = os.environ['FeedbackURL']

def sendfeedback(feedback: str, user: str, id: int):
  data = {
      "content" : feedback,
      "username" : "{" + user + "}" + ", " + "(" + str(id) + ")"
  }
  result = requests.post(url, json = data)
