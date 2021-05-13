import requests

def main():
    url = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com"
    req = requests.get(url)
    print(req.text)

main()