#create flash card game
#import json data file 
import json
import random
import os
import glob

is_running = True
score = 0
dir_path = os.path.join(os.path.dirname(__file__), 'json-data')

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

while is_running:
    #get the length of json file in json-data folder
    total = len(get_json("hiragana.json")["quiz"])
    #random number from 0 to total
    num = random.randint(0, total - 1)
    guess = input(get_json("hiragana.json")["quiz"][num]["q"] + " = ")
    if(guess == get_json("hiragana.json")["quiz"][num]["a"]):
        print("Correct")
        score += 1
    else:
        print("Wrong the answer is", get_json("hiragana.json")["quiz"][num]["a"])
        print("total score ", score)
        
        break
    
    
    