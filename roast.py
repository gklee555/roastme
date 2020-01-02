from roast_csv_reader import *
import numpy as np
import matplotlib.pyplot as plt 
import random
import re

HEAT_INDEX = 1000

class RoastMachine:
    def __init__(self, path="./roasts.csv"):
        self.path = path
        self.all_roasts = self.get_all_roasts()
        self.sick_burns = self.get_sick_burns()

    # Reads all roasts from roasts.csv, run "python3 scrape.py" to create roasts.csv
    def get_all_roasts(self):
        return read_roasts(self.path)
    
    # removes special characters, edits, and links
    def clean_roasts(self, roasts):
        clean_roasts = []
        for roast in roasts:
            r_text = roast[-1]
            edit_search = re.search("\nedit", r_text, re.IGNORECASE)

            if edit_search:
                r_text = r_text[0:edit_search.span()[0]]
            # removing white spaces and newline stuff 
            r_text = " ".join(r_text.split())

            if not re.findall('http[s]?://', r_text) and re.search("you", r_text, re.IGNORECASE):
                clean_roast = (roast[0], roast[1], roast[2], roast[3], r_text)
                clean_roasts.append(clean_roast)
        return clean_roasts 

    def get_sick_burns(self):
        sick_burns = []
        scores = []
        replies = []
        all_roasts_clean = self.clean_roasts(self.all_roasts)
        for roast in all_roasts_clean:
            (id, score, reply, isGilded, roasts) = roast
            heat = int(score)
            if (heat > HEAT_INDEX):
                sick_burns.append(roast)
                scores.append(int(score))
                replies.append(int(reply))
        return sick_burns
    # returns a string roast of a person 
    def roast(self):
        return random.choice(self.sick_burns)
    def write_sick_burns(self, path):
        with open(path, "w", newline="") as f:
            writer = csv.writer(f, delimiter=" ", quotechar="|", quoting=csv.QUOTE_MINIMAL)
            writer.writerow(["Id", "Score", "Replies", "isGilded", "Roasts"])

            for roast in self.sick_burns:
                writer.writerow(roast)
    def roast(self):
        return random.choice(self.sick_burns)[-1]

if __name__=="__main__":
    rm = RoastMachine()
    print(rm.roast())
    rm.write_sick_burns("./sick_burns.csv")

    r_you = []
    r_no_you = []
    for roast in rm.sick_burns:
        roast_txt = roast[-1]
        if re.search("you", roast_txt, re.IGNORECASE):
            r_you.append(roast)
        else:
            r_no_you.append(roast)
    
    for r in r_no_you:
        print(r[-1])
    print("\n\nWITH YOU")
    for r in r_you:
        print(r[-1])