import requests

def downloader():
    url = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.csv"
    down_file = requests.get(url)
    local_file = "agg_data.csv"

    with open(local_file, 'wb')as file:
        file.write(down_file.content)

def parseer():
    with open("agg_data.csv", "r") as file:
        read_list = file.readlines()
        print(read_list)

def main():
    downloader()
    parseer()

main()