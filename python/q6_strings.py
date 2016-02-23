def donuts(count):
    if count < 10:
        output = str(count)
    else:
        output = 'many'
    return 'Number of donuts: '+ output

def both_ends(s):
    if len(s) < 2:
        return ''
    else: 
        return s[:2]+s[-2:]

def fix_start(s):
    temp = s[0]
    new =''
    for i in s:
        if i==temp:
            new = new + '*'
        else:
            new = new + i
    return s[0] + new[1:]

def mix_up(a,b):
    first = b[:2]+a[2:]
    second =a[:2]+b[2:]
    return first + ' ' + second

def verbing(s):
    if len(s) > 2 and s[-3:] != 'ing':
        return s + 'ing'
    elif len(s) > 2:
        return s + 'ly'
    else:
        return s

def not_bad(s):
    first = s.find('not')
    second = s.find('bad',first+2)
    if first and second > 0:
        return s[:first] + 'good' + s[second+3:]
    return s

def front_back(a,b):
    index1=len(a) - int(len(a)/2)
    index2=len(b) - int(len(b)/2)
    return a[:index1] + b[:index2] + a[index1:] + b[index2:]
