import requests
#import pandas

local_file = "agg_data.csv"

def downloader():
    url = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.csv"
    down_file = requests.get(url)

    with open(local_file, "wb")as writer:
        writer.write(down_file.content)

def parseer():
    with open(local_file, "r") as reader:
        #Converting the file to a list, line 1 will be index 0, so on and so forth
        all_lines = list(reader)
        t = 0
        for i, l in enumerate(all_lines):
            line = all_lines[i - 1]
            print(line)
            t += 1
            print(t)
            if t > 20:
                break
            

def main():
    downloader()
    parseer()

main()