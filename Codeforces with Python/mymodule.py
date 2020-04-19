def nextPali(a):
        if len(a)==1 and a!='9':
            result=int(a)+1
        elif ''.join(set(a))=='9':
            lena=len(a)
            result=int(a)+2
        else:
            if len(a)%2==0:
                lena=len(a)//2
                head=a[:lena]

                if head+head[::-1]>a:
                    result=head+head[::-1]
                else:
                    while head+head[::-1]<=a:
                        head=str(int(head)+1)
                    result=head+head[::-1]           
            else:
                lena=len(a)//2
                head=a[:lena]
                mid=a[lena]

                if head+mid+head[::-1]>a:
                    result=head+mid+head[::-1]
                else:
                    while head+mid+head[::-1]<=a:
                        mid=str(int(mid)+1)
                        if mid=='10':
                            head=str(int(head)+1)
                            mid='0'
                    result=head+mid+head[::-1]
        return result
