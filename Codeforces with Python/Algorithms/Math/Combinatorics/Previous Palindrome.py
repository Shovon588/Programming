n=int(input())

def Previous_Palindrome(num):
    for x in range(num-1,0,-1):
        if str(x) == str(x)[::-1]:
            return x
        
print(Previous_Palindrome(n))
