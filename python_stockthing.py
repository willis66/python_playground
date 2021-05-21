
import requests
import collections
from datetime import date, datetime

local_file = "agg_data.csv"
main_dict = {}
past_date = datetime.strptime(input("how far back do you want to go (yyyy-mm-dd): "), "%m/%d/%Y")

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
        for line_num, content in enumerate(all_lines):
            content = cleanup_string_from_list(content)
            #print(line_num)
            #print(content)
            #Takes the first line (which should contain keys) and converts it to a list which is placed inside a dictionary
            line_list = content.split(",")
            if line_num == 0:
                for i, l in enumerate(line_list):
                    main_dict[l] = []
            else:
                for i, l in enumerate(line_list):
                    #add dumb shit error handling
                    try:
                        if date_finder(line_list[0]):#linenum[0] should be the date 
                            list(main_dict.values())[i].append(l)
                            #Adding whatever then removing blank strings
                            list(main_dict.values())[i].remove("")
                    except:
                        pass
                        #it does throw errors/make mistakes often, but i don't care enough

def cleanup_string_from_list(string):
    string = string.replace("\n", "")
    string = string.replace(",0", "0")#cleaning up money
    string = string.replace("N/A", "")
    string = string.replace("--", "")
    #A lot of exceptions where dumbasses *cough* senators *cough* put in random commas, I've just added a try except: pass above as most dont matter to me
    return string

def data_output():
    #prob gonna make it output to a file for now
    print(main_dict.keys())
    counted_dict = collections.Counter(main_dict[input("what key: ")])
    output_file = "output_file.txt"
    with open(output_file, "w") as writer:
        #use: counted_dict.items() for #alphabetical
        for i in sorted(counted_dict, key=counted_dict.get, reverse=True):
            #writer.write(i + str(l) + "\n") #alphabetical
            writer.write(i + " : " + str(counted_dict[i]) + "\n")

def main():
    #should set up to run periodically
    downloader()
    parseer()#this one takes a while to run currently
    data_output() 

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

main()