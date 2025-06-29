import requests

r = requests.get('https://www.cricbuzz.com/live-cricket-scores/105762/ind-vs-eng-1st-test-india-tour-of-england-2025')
print(r.text)   #generally extracts html code

with open("cricbuzz.txt", "w") as Write:
  Write.write(r.text)