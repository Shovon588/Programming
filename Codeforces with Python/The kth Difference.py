n=int(input())

evenLow=(n*(n-1))+2
evenHigh=evenLow+(n-1)*2
oddLow=(n*(n-1))+1
oddHigh=oddLow+(n-1)*2

a=[]

if n%2==0:
    evenSum=int((evenHigh+evenLow)*(n/2))
    oddSum=int((oddHigh+oddLow)*(n/2))

    print(evenSum-oddSum)

else:
    evenSum=((evenHigh+evenLow)*(n/2))+(evenHigh+evenLow)
    oddSum=((oddSum+oddLow)*

    
    
