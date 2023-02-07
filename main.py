import re
import os
#print(bcolors.FAIL + "SYSERROR: FAILED TO READ FILE, CHECK IF FILE IS CORRUPTED" + bcolors.ENDC)

real_path = os.path.realpath(__file__)
dir_path = os.path.dirname(real_path)

list_of_queries = []
for file in os.listdir(os.path.join(dir_path, "filesystem")):
    tmp = file.replace(".txt", "").replace("_", " ")
    list_of_queries.append(tmp)

print(list_of_queries)


class bcolors:
    HEADER = '\033[95m'
    OKBLUE = '\033[94m'
    OKCYAN = '\033[96m'
    OKGREEN = '\033[92m'
    WARNING = '\033[93m'
    FAIL = '\033[91m'
    ENDC = '\033[0m'
    BOLD = '\033[1m'
    UNDERLINE = '\033[4m'


def process_query(query):
    try:
        path = os.path.join(dir_path, "filesystem/" + query.lower().replace(" ", "_") + ".txt")
        list_of_queries_edit = [query3 for query3 in list_of_queries if query3 != query]
        page = open(path)
        for line in page:
            for query2 in list_of_queries_edit:
                query_len = len(query2)
                index = line.lower().find(query2.lower())
                if index > 0:
                    line = line[:index] + bcolors.OKCYAN + line[index:index+query_len] + bcolors.ENDC + line[index+query_len:]

            print(line.replace("\n", ""))

    except:
        print(bcolors.FAIL + "QUERY NOT FOUND" + bcolors.ENDC)


def startup():
    logo = "\n .d88888b.  \nd88P\" \"Y88b \n888     888 \n888     888 \n888     888 \n888 Y8b 888 \nY88b.Y8b88P \n \"Y888888\"  \n       Y8b  \n"
    print(logo)
    print("QUEWARDS SCHOOL DATABASE ARCHIVE\n" + bcolors.FAIL + "EMERGENCY RECOVERY MODE ACTIVE" + bcolors.ENDC)
    print(bcolors.WARNING + "IMAGES HAVE BEEN PURGED TO SAVE SPACE")
    print(bcolors.OKGREEN + "Welcome to the Quewards School Database!\nQuery \"help\" to get started\n" + bcolors.ENDC)

def main_loop():
    query = input(">>> ")
    if query != "quit" and query != "exit":
        print("")
        process_query(query)
        print("")
    return query

startup()
query = ""
while query != "quit" and query != "exit":
    query = main_loop()
