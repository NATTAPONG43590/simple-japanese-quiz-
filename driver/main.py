import json
import random
import os
import glob

#initial variables declaration
score = 0
dir_path = os.path.join(os.path.dirname(__file__), 'json-data')
temp = None
answered_item = []
file_name = "hiragana.json"
try_per_queston = 2

#json function module
#get the list of json file in json-data folder
def get_json_list():
    json_list = []
    for file in glob.glob(os.path.join(dir_path, '*.json')):
        json_list.append(os.path.basename(file))
    return json_list
#get the json file in json-data folder
def get_json(file_name):
    
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'r' , encoding="utf8") as file:
        data = json.load(file)
    return data
while True:
    #get the length of json file in json-data folder
    try:
        total = len(get_json(file_name)["quiz"])
    except KeyError:
        print("Error: pls. change the json file name to quiz before start this program")
        break   

    #random number from 0 to total
    rand_num = random.randint(0, total - 1)
    while answered_item.count(rand_num) == try_per_queston and len(answered_item) != total * try_per_queston:
        rand_num = random.randint(0, total - 1)
    num = rand_num 
    answered_item.append(num)
    guess = input(get_json(file_name)["quiz"][num]["q"] + " = ")
    if(guess.lower() == "ex"):
        break
    elif(guess.lower() == get_json(file_name)["quiz"][num]["a"]):
        print("Correct")
        score += 1
    else:
        if(guess == ""):
            print("You didn't enter anything")
        else:
            print("Incorrect")
        
        print("the answer is", get_json(file_name)["quiz"][num]["a"])    
        print("total score ", score)
        score = 0
            
    print(len(answered_item) , "/" , total * try_per_queston ,"[",answered_item.count(rand_num),"/",try_per_queston,"]")
    if(len(answered_item) == total * try_per_queston):
        print("You have completed the quiz type 'ex' or crtl+c to exit")
        answered_item = []
    