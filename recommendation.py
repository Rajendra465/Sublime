import json
import pandas as pd
import sys
import json
x = sys.argv[1]
subject = sys.argv[2]
Question_Data = pd.read_json('nedgen.json')
Question_Data = pd.DataFrame(Question_Data)

y=json.loads(json.dumps(x))

User_Data = pd.read_json(y)

sum_ = 0
User_Data['Ratio'] = 0
for i, j in zip(User_Data['percent'], User_Data['Ratio'].index):
    if int(i) <= 50:
        User_Data['Ratio'][j] = 3
        sum_ = sum_ + 3
    elif int(i) > 50 and int(i)< 80:
        User_Data['Ratio'][j] = 2
        sum_ = sum_ + 2
    elif int(i) >= 80:
        User_Data['Ratio'][j] = 1
        sum_ = sum_ + 1


No_of_ques = []
for i in User_Data['Ratio']:
    temp_ques_no = int((30/sum_)*i)
    No_of_ques.append(temp_ques_no)

sumt = sum(No_of_ques)

left_ques = 30 -sumt


if sumt< 30:
    for k in range(0,len(No_of_ques)): 
        if left_ques> 0:
            No_of_ques[k] = No_of_ques[k] + (left_ques//left_ques)
            
            left_ques = left_ques - 1
framesy =[]
for i,j in zip(User_Data['section'],No_of_ques):
    wtt = Question_Data.loc[Question_Data['Section'] == i] 
    wttt = wtt.sample(n=j)
    framesy.append(wttt)
frame = pd.concat(framesy)
xyz = frame.to_dict('records')
print(json.dumps(xyz))
