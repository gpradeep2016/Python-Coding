import json

##### Data acquisition and parsing ######
with open('notes/team_history.json') as f:
    hist = json.load(f)

record = [game['result'] for game in hist]
scores = [game['score'] for game in hist]
dates = [game['date'] for game in hist]

##### Data analysis #######################    
print len(scores), sum(scores), min(scores), max(scores), scores[0], scores[-1]
print len(record), record[0], record[-1], record.count('lost')
print len(dates), dates[0], dates[1]
