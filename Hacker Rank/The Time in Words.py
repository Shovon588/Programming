hour = int(input())
minute = int(input())

strHour = {1: 'one', 2: 'two', 3: 'three', 4: 'four',
           5: 'five',6: 'six', 7: 'seven', 8: 'eight',
           9: 'nine',10: 'ten',11: 'eleven',12: 'twelve'}


strMin = {1:'ten', 2: 'twenty', 3:'thirty', 4:'fourty', 5:'fifty'}

strTeen = {11:'eleven', 12: 'twelve', 13:'thirteen',
           14:'fourteen', 15:'fifteen', 16:'sixteen',
           17:'seventeen',18:'eighteen', 19:'nineteen'} 


if minute==0:
    hou = strHour[hour]
    res = hou + " o' clock"
elif minute%10==0 and minute!=30:
    if minute>30:
        hou = strHour[hour+1]
        minu = strMin[(60-minute)//10]
        res = minu +' minutes to ' + hou
    else:
        hou = strHour[hour]
        minu = strMin[minute//10]
        res = minu +' minutes past ' + hou
        
elif minute==15:
    hou = strHour[hour]
    res = 'quarter past ' + hou
elif minute==45:
    hou = strHour[hour+1]
    res = 'quarter to ' + hou
elif minute==30:
    hou = strHour[hour]
    res = 'half past ' + hou
elif minute>=11 and minute<=19:
    minu = strTeen[minute]
    hou = strHour[hour]
    res = minu +' minutes past ' + hou
elif minute==1:
    hou = strHour[hour]
    res = 'one minute past ' + hou
elif minute>=2 and minute<=9:
    minu = strHour[minute]
    hou = strHour[hour]
    res = minu + ' minutes past ' + hou
else:
    hou = strHour[hour]
    if minute<30:
        first = str(minute)[0]
        second = str(minute)[1]
        string = strMin[int(first)]
        string = string + ' ' + strHour[int(second)]
        res = string+' minutes past '+hou
    else:
        minute = 60-minute
        hou = strHour[hour+1]
        if minute<10 and minute>1:
            minu = strHour[minute]
            res = minu+' minutes to '+hou
        elif minute==1:
            res = 'one minute to '+hou
        elif minute>=11 and minute<=19:
            minu = strTeen[minute]
            res = minu+' minutes to '+hou
        else:
            first = str(minute)[0]
            second = str(minute)[1]
            string = strMin[int(first)]
            string = string + ' ' + strHour[int(second)]
            res = string+' minutes to '+hou
            
        
