print("Hello SRC Department!")
#new changes
print("Hello SRC Department!")

import pandas as g
#read.csv("C:\\Users\\Bhoilkar\\Desktop\\sam assignments\\Data_analysis\\Max Reach - HR Activity.csv")

sheet_link= "sheet"
# /edit?usp=sharing
#   1FSDcawX8j_SM4BKjvwB3QzSVTR0mh7EvqO2WFj7bpSo
#df = g.read_csv(r'shubhambhoilkar/Database/blob/main/Max%20Reach%20-%20HR%20Activity.xlsx.csv')

#df = g.read_csv(f"https://docs.google.com/spreadsheets/d/{sheet_link}/export?format=csv")
#print(g)
# 
dict_core ={"Day0":(0,1,0,1),
           "Day1":(1,1,1,0),
           "Day2":(1,0,0,0),
           "Day3":(0,0,0,0),
           "Day4":(0,0,0,1),
           "Day5":(1,1,1,1)}

print(dict_core)
#print(sum(dict_core.values()))

#separation of dictionaries values
Day0,Day1,Day2,Day3,Day4,Day5=dict_core["Day0"],dict_core["Day1"],dict_core['Day3'],dict_core['Day4'],dict_core['Day4'],dict_core['Day5']
print(Day0,Day1,Day2,Day3,Day4,Day5)
print(type(Day0))

#Addition of dictionary values(tuple values)
result=tuple(map(lambda a,b,c,d,e,f:a+b+c+d+e+f,Day0,Day1,Day2,Day3,Day4,Day5))
print(result)
shubham =(1,0,0,1) 
vaishnav =(0,0,1,0)
kanchan=(1,0,1,1)
vaishnavi=(0,0,1,1)
sairaj=(1,1,0,0)
print(shubham,vaishnav,kanchan,sairaj,vaishnavi)
names={shubham,vaishnav,kanchan,sairaj,vaishnavi}
print(names)

if shubham[0]==1 and shubham[1]==1 and shubham[2]==1 and shubham[3]==1:
    print("interaction is positive")
    print("interaction was negative")
    print("interaction was neutral")
    print("interaction should be avoidable")
elif shubham[0]==0 and shubham[1]==0 and shubham[2]==0 and shubham[3]==0:
    print("Interaction was empty")
else:
    print("Interaction was invalid")

#elif shubham[0]==1 and shubham[1]==1 and shubham[2]==1 and shubham[3]==1:
#addition_of_tuples = tuple(sum(shubham,sum(vaishnav,sum(kanchan,sum(sairaj,vaishnavi)))))
result = tuple(map(lambda a,b,c: a+b+c,shubham, vaishnav,sairaj))
print(result)
