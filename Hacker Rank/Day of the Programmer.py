n = int(input())


def dayOfProgrammer(year):
    leap = "12.09."+str(year)
    notLeap = "13.09."+str(year)

    if year%4==0:
        return leap
    else:
        return notLeap

print(dayOfProgrammer(n))
