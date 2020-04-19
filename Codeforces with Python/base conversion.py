def conv(num,b):
    convStr = "0123456789abcdefghijklmnopqrstuvwxyz"
    if num<b:
        return convStr[num]
    else:
        return conv(num//b,b) + convStr[num%b]
