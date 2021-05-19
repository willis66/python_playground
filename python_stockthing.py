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
        read_list = reader.readlines()
        #print(read_list)

def main():
    downloader()
    parseer()

main()