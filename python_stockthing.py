
import requests
import collections

local_file = "agg_data.csv"
main_dict = {}

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
            if line_num == 0:
                #Takes the first line (which should contain keys) and converts it to a list which is placed inside a dictionary
                line_list = content.split(",")
                for i, l in enumerate(line_list):
                    main_dict[l] = []
            else:
                line_list = content.split(",")
                for i, l in enumerate(line_list):
                    #add dumb shit error handling
                    try:
                        list(main_dict.values())[i].append(l)
                        #Adding whatever then removing blank strings
                        list(main_dict.values())[i].remove("")
                    except:
                        pass

def cleanup_string_from_list(string):
    string = string.replace("\n", "")
    string = string.replace(",0", "0")
    string = string.replace("N/A", "")
    string = string.replace("--", "")
    #A lot of exceptions where dumbasses *cough* senators *cough* put in random commas, I've just added a try except: pass above as most dont matter to me
    #string = string.replace(", ", "; ")
    #string = string.replace(',"', "")
    return string
            

def main():
    downloader()
    parseer()
    data_output()


def data_output():
    #prob gonna make it output to a file for now

main()
print(main_dict.keys())
print(collections.Counter(main_dict[input("what key: ")]))
