n,p = map(str,input().split())
n = int(n)
p = float(p)


prob_happy = 1
while n>0:
    if n%2==1:
        prob_happy = prob_happy * (1-p) + (1-prob_happy) * p
        # p = possibility of mood swing
        # 1-p = possibility for not swinging the mood
        # prob_happy = probability of being happy at that moment
        # 1-prob_happy = probability of not being happy at that moment

    p = p * (1-p) + p * (1-p)
    n = n//2

print(prob_happy)

