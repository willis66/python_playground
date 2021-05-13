import requests

def main():
    url = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.csv"
    down_file = requests.get(url)
    local_file = "agg_data.csv"

    with open(local_file, 'wb')as file:
        file.write(down_file.content)

main()