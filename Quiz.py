import requests
import json
import pprint
import html
import random

url="https://opentdb.com/api.php?amount=1&category=21&difficulty=easy&type=multiple"
d=0
z=True
while(z==True):
    valid_answer=False
    continue_now=False
    r=requests.get(url)
    n=json.loads(r.text)
    a=n['results'][0]['question']
    print("\n"+html.unescape(a))
    print("\nChoose the right answer:\n")
    b=n['results'][0]['correct_answer']
    c=n['results'][0]['incorrect_answers']
    c.append(b)
    random.shuffle(c)
    answer_number=1
    #answers={'1':c[0],'2':c[1],'3':c[2],'4':c[3]}
    for i in range(len(c)):
        print(str(answer_number)+ '. ' +html.unescape(c[i]))
        answer_number+=1
    while(valid_answer==False):
        w=input("\nEnter your choice: ")
        try:
            w=int(w)
            if(w>len(c) or w<=0):
                print("\nInvalid number.\n")
            else:
                valid_answer=True
        except:
            print("Invalid answer. Use only numbers")
    
    if(w==1 and b==c[0]):
        print("\nCorrect answer.")
        d=d+1
    elif(w==2 and b==c[1]):
        print("\nCorrect answer.")
        d=d+1
    elif(w==3 and b==c[2]):
        print("\nCorrect answer.")
        d=d+1
    elif(w==4 and b==c[3]):
        print("\nCorrect answer.")
        d=d+1
    else:
        print("\nIncorrect answer.")
        print("\nThe correct answer is" , b)

    while(continue_now==False):
        again=input("\nDo you want to continue (y/n)? ")
        try:
            if(again=='y'):
                print("\n")
                for j in range(80):
                    print('-',end="")
                print('\n')
                continue_now=True
            elif(again=='n'):
                print("\n")
                for j in range(80):
                    print('-',end="")
                print('\n')
                continue_now=True
                z=False
                print("Until next time!\n")
            #if(again=='n'):
                #break
            #elif(again=='y'):
                #continue
        except:
            print("\nInvalid input, try again\n")


print("Your score is :" , d , "\n")
