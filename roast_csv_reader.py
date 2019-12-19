import csv

def read_roasts(path):
    roasts = []
    with open(path, newline='') as f:
        reader = csv.reader(f, delimiter=" ", quotechar="|")
        for row in reader:
            roast = (row[0], row[1], row[2], row[3], row[4]) 
            roasts.append(roast)
    print(roasts)
    print(len(roasts))
    return roasts
if __name__=="__main__":
    read_roasts("./roasts.csv")