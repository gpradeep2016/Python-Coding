"Learn common regex data extraction patterns"

import re

##### Data acquisition ##################
with open('notes/team_history.txt') as f:
    hist = f.read()

##### Data parsing #######################
record = re.findall(r'won|lost', hist)
dates = re.findall(r'[0-9]+/[0-9]+/[0-9]+', hist)
scores = []
for score_string in re.findall(r'(\d+) point', hist):
    scores.append(int(score_string))

##### Data analysis #######################    
print len(scores), sum(scores), min(scores), max(scores), scores[0], scores[-1]
print len(record), record[0], record[-1], record.count('lost')
print len(dates), dates[0], dates[1]

