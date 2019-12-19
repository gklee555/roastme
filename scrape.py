#! usr/bin/env python3
import praw
import pandas as pd
import datetime as dt
import getpass
import csv 
# Variables or somthing 
DEBUG = False 
SCORE_THRESH = 1500
REPLIES_THRESH = 2
MAX_LEN = 240 
# Get reddit 
pass_attempts =0
while (pass_attempts<3):
    pass_attempts += 1
    try:
        p = getpass.getpass() # read yo password bitch
        reddit = praw.Reddit(client_id='u_4sDiZA8iMyJg', \
                        client_secret='vNxucLVAqajSMnKs8ajiLG1EXxs', \
                        user_agent='roast_machine', \
                        username='hot_soft_pretzel', \
                        password=p)
        for test in reddit.subreddit("all").top(limit=1): # Check that the connection was successful 
            (test.title)
        pass_attempts = 5
    except Exception as error:
        print("Wrong password or something, try again bumbly finger ass!\n")
        if DEBUG: 
            print("btw here's your error : ", error)
p = "" # clear the password. Not sure if important 

# Get roast me 
roastme = reddit.subreddit("RoastMe")

# Get top posts 
posts = roastme.top(time_filter="all", limit=3)

# store bests roasts and some data
roasts = []
ids = []
scores = []
is_gilded = []
count = 0
for post in posts:  # iterate over top posts 

    comments = post.comments # Get all comments from the top post 

    for tlc in comments: # for each top level comment
        try:
            tlc.distinguished
        except:
            print(tlc)
            break
        if (tlc.distinguished =="moderator"): # ignore if it's moderator 
            print("ignoring moderator")
            pass
        elif (tlc.is_submitter): # comment is not from op
            print("ignoring OP")
            pass
        else:  # store fire ass roast 
            count += 1
            is_gilded.append(tlc.gilded)
            roasts.append(tlc.body)
            ids.append(tlc.id)
            scores.append((tlc.score, len(tlc.replies)))
    


with open('roasts.csv', "w", newline="") as f:
    writer = csv.writer(f, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Id","Score", "Replies", "isGilded", "Roasts"])

    for i in range(len(ids)):
        writer.writerow([ids[i]] + [str(scores[i][0])] + [str(scores[i][0])] + [str(is_gilded[i])] + [roasts[i]] )

