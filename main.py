logs=[]

def liitumine(a,b):
    logs.append('liitumine')
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a+b
print(liitumine(5,5))

def lahutamine(a,b):
    logs.append('lahutamine')
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a-b
print(lahutamine(5,'5'))

def korrutamine(a,b):
    logs.append('korrutamine')
    if isinstance(a,str) or isinstance(b,str):
        print("vale andmed")
        return ""
    return a*b
print(korrutamine(5,5))

def jagamine(a,b):
    logs.append('jagamine')
    try:
        if isinstance(a,str) or isinstance(b,str):
            print("vale andmed")
            return ""
        return a/b
    except ZeroDivisionError:
        print("ei saa jagada nullile")
print(jagamine(5,5))

def logsKuvamine(logs):
    jag=0
    kor=0
    liit=0
    lahut=0
    for elem in logs:
        if elem=='korrutamine':
            kor +=1
        elif elem=='lahutamine':
            lahut +=1
        elif elem=='liitumine':
            liit +=1
        else: 
            jag +=1
    return [jag, kor, liit, lahut]
print(logsKuvamine(logs))