import random

key = [' '] * 9
print('Количество ключей:')
k = input()
try:
    k = int(k)
except ValueError:
    k = 1

def umnozhenie():
    r = random.randint(0,9)
    i = random.randint(0,9) 
    while (i * r > 9):
        r = random.randint(0,9)
        i = random.randint(0,9)    
    return r, i

def slozhenie():
    r = random.randint(0,9)
    i = random.randint(0,9) 
    while (i + r >9):
        r = random.randint(0,9)
        i = random.randint(0,9)    
    return r, i

def vichitanie():
    r = random.randint(0,9)
    i = random.randint(0,r)
    while (r - i < 0):
        r = random.randint(0,9)
        i = random.randint(0,r)  
    return r, i

def delenie():
    r = random.randint(0,9)
    if (r == 0):
        i = 1
    else:
        i = random.randint(1,r)
        
    while (r % i != 0):
        r = random.randint(0,9)
        if (r == 0):
            i = 1
        else:
            i = random.randint(1,r)
            
    return r, i

n=0

while n < k:
    a1 = random.randint(1,2)
    a2 = random.randint(1,4)
    if (a1 == 1):
        key[2] = '='
    
        if(a2 == 1):
            key[6] = '*'
            key[4], key[8] = umnozhenie()
            key[0] = key[4] * key[8]
    
        if(a2 == 2):
            key[6] = '+'
            key[4], key[8] = slozhenie()
            key[0] = key[4] + key[8]
        
        if(a2 == 3):
            key[6] = '-'
            key[4], key[8] = vichitanie()
            key[0] = key[4] - key[8]
        
        if(a2 == 4):
            key[6] = '/'
            key[4], key[8] = delenie()
            key[0] = key[4] // key[8]
        
    
    else:
        key[6] = '='
    
        if (a2 == 1):
            key[2] = '*'
            key[0], key[4] = umnozhenie()
            key[8] = key[0] * key[4]
    
        if (a2 == 2):
            key[2] = '+'
            key[0], key[4] = umnozhenie()
            key[8] = key[0] + key[4]
        
        if (a2 == 3):
            key[2] = '-'
            key[0], key[4] = vichitanie()
            key[8] = key[0] - key[4]
    
        if (a2 == 4):
            key[2] = '/'
            key[0], key[4] = delenie()
            key[8] = key[0] // key[4]

    print(''.join([str(i) for i in key]))
    n += 1




