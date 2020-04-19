import random,time
words=['shovon','hello','from','the','other','side','ruet','RUET','Ece',"don't",'side','beside','though','although','player','movement','tales',
       'story','being','able','talk','score','sports','fitness','gym','lieutenant','sergent','mosque','charch','school','river','monkey',
       'tubewell','gate','and','or','not','electrical','computer','tales','engineering','education','scholarship','sportsmanship','hunt','deer','tiger','elephant','cat','dog']



count=0
start=time.time()
for i in range(100):
    a=random.randint(0,49)
    b=words[a]
    print(b)
    
    put=input()
    
    if put==b:
        count+=1
    end=time.time()

    if end-start>=60:
        break




print('Total task=',i+1,'   Correct answer',count,'    Wrong answer=',i-count+1,'   Time=',end-start)
