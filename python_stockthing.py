#check for multiple reports of the same thing (ptr link should be unique)#not done
#upgrading to csv reader#upgraded
import requests
import collections
from datetime import date, datetime
import csv

local_file = "agg_data.csv"
main_dict = {}

output_file = "output_file.txt"
with open(output_file, 'w') as clear:#clears output file
    pass

while True:
    try:
        past_date = datetime.strptime(input("how far back do you want to go (mm/dd/yyyy): "), "%m/%d/%Y")
        break
    except:
        print("real date please")

def downloader():
    url = "https://senate-stock-watcher-data.s3-us-west-2.amazonaws.com/aggregate/all_transactions.csv"
    down_file = requests.get(url)

    with open(local_file, "wb")as writer:
        writer.write(down_file.content)

def parseer():
    with open(local_file, "r") as file:
        csv_dict = csv.DictReader(file)#, delimiter = ",", quotechar = '"'
        #Converting the file to a list, line 1 will be index 0, so on and so forth
        for things in csv_dict:
            try:
                if date_finder(things['transaction_date']) and is_ticker(things['ticker']):
                    data_output(str(things) + '\n')
                    #print(things['ticker'])
            except:
                pass

def data_output(in_string):
    with open(output_file, "a") as writer:
        writer.write(in_string)

def main():
    #should set up to run periodically
    downloader()
    parseer()#this one takes a while to run currently #and would take a lot of extra work to forgo the commas

def date_finder(in_date):
    #i dont want to spend that much time on this
    status = False
    in_date = datetime.strptime(in_date, "%m/%d/%Y")
    current_date = date.today()
    days_back = current_date - past_date.date()
    days_calc = current_date - in_date.date()

    if days_calc <= days_back:
        status = True

    return status

def is_ticker(in_ticker):
    status = True
    if in_ticker == "N/A" or in_ticker == "--" or in_ticker == "":
        status = False

    return status

main()
