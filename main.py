def Add_Number_Sequence(n):
    if n == 0:
        return 0
    else:
        return Add_Number_Sequence(n//10) + (n%10)

def Reverse_Number_Sequence(n):
    m = 10**len(str(n))
    if n == 0:
        return 0
    else:
        return (Reverse_Number_Sequence(n//10) + ((n%10)*m)//10)

print(Add_Number_Sequence(1234))
print(Reverse_Number_Sequence(1234))
