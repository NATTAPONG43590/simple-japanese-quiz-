import json
import random
import os, sys
import glob
import time
import numpy as np
#initial variables declaration
score = 0
dir_path = os.path.join(os.path.dirname(__file__), 'json-data')
temp = None
answered_item = np.array([])
wrong_ans = np.array([])
file_name = "hiragana.json"
try_per_queston = 1
sec =0
attemp = 0
retry = 3
time_taken_per_question = np.array([])
#json function module
#get the list of json file in json-data folder
def get_json_list():
    json_list = np.array([])
    for file in glob.glob(os.path.join(dir_path, '*.json')):
        json_list.append(os.path.basename(file))
    return json_list
#get the json file in json-data folder
def get_json(file_name):
    
    file_path = os.path.join(dir_path, file_name)
    with open(file_path, 'r' , encoding="utf8") as file:
        data = json.load(file)
    return data
#check ans function
def check(ans):
    if(ans.lower() == get_json(file_name)["quiz"][num]["a"]):
        return True
    else:
        # na
            # print("You didn't enter anything")
        return False

def progressBar(current, total, barLen=20):
    percent = float(current) / total
    hashes = '#' * int(round(percent * barLen))
    spaces = ' ' * (barLen - len(hashes))
    sys.stdout.write("\rPercent: [{0}] {1}%".format(hashes + spaces, int(round(percent * 100))))
    sys.stdout.flush()
    print("\n")
    
while True:
    attemp += 1
    start = time.time()
    
    #get the length of json file in json-data folder
    try:
        total = len(get_json(file_name)["quiz"])
    except KeyError:
        print("Error: pls. change the json file name to quiz before start this program")
        break   

    #random number from 0 to total
    rand_num = random.randint(0, total - 1)
    #count element in answered_item
    
    while np.count_nonzero(answered_item == rand_num) == try_per_queston and len(answered_item) != total * try_per_queston:
        rand_num = random.randint(0, total - 1)
    num = rand_num 
    
    guess = input(get_json(file_name)["quiz"][num]["q"] + " = ")
    os.system('CLS')
    if(guess.lower() != "ex" and check(guess) != None):
        if(check(guess)):
            GREEN = '\033[32m'
            print(GREEN + "Correct" + '\033[0m')
            answered_item = np.append(answered_item, num)
            score += 1
            color = GREEN
            colorB = '\033[0m'
        else: 
            wrong_ans = np.append(wrong_ans, num)
            CRED = '\033[91m'
            CEND = '\033[0m'
            color = CRED
            colorB = CEND
            print(CRED + "Incorrect" + CEND)
            print("the answer is", get_json(file_name)["quiz"][num]["a"])    
            print("total score ", score)
            
            # score = 0
            # answered_item = []
            # break
    
      
        
        accuracy = round((score / attemp) * 100, 2)
        sec = time.time()
        time_taken_per_question = np.append(time_taken_per_question, round(sec-start,2))
        
        print(color+"Accuracy: ", accuracy, "%"+colorB)
        print("Time Taken", time_taken_per_question[-1] , "seconds")
        print("Average time taken per question: ", round(np.mean(time_taken_per_question),2), "seconds")
        progressBar(len(answered_item), total, barLen=20)
        # print(len(answered_item) , "/" , total * try_per_queston ,"[",answered_item.count(rand_num),"/",try_per_queston,"]")
        if(attemp == total * try_per_queston):
            if(len(wrong_ans) == 0):
                print("You have completed the quiz type 'ex' or crtl+c to exit")
                break    
    else:
        break  
