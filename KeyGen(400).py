#!/usr/bin/env python
# coding: utf-8



import random;

var = []




for a in range(0,9):
    for b in range(0,9):
        for c in range(0,9):
            for d in range(0,9):
                k = a + b + c + 4*d
                var.append(str(a)+str(b)+str(c)+str(d))
                var.append(str(k))
                




count = 0
max = 0
key = []
print("Enter how many keys you want to generate(recomended maximum is 20):")
max = input()

try:
    max = int(max)
except ValueError:
    max = -1
max = int(max)
    
if (max>20) or (max < 1):
    max = 20
    print("20 keys will be generated anyway :)")
end = 0
print("Starting generating keys(It may take a while)...")
while (count < max):
    n = []
    while (len(n) < 4):
        l = random.randint(0,64)
        for i in range(0,len(var)):
            if (str(l) == var[i]):
                n.append(var[i-1])
    #print(n)
    for a in range(0,len(n)):
        for b in range(0,len(n)):
            for c in range(0,len(n)):
                for d in range(0,len(n)):
                    s = n[a] + "-" + n[b] + "-" + n[c] + "-" + n[d]
                    s = str(s)
                    flag = 0
                    for i in range(0,3+1):
                        if ((s[i] == s[i+5]) or (s[i] == s[i+10]) or (s[i] == s[i+15])):
                            flag = 1
                        if ((s[i+5] == s[i+10]) or (s[i+5] == s[i+15])):
                            flag = 1
                        if (s[i+10] == s[i+15]):
                            flag = 1
                    if (flag == 0):
                        key.append(s)
                        #print(s)
                        count += 1
                        print("Generated: " + str(count))
                    if (count>= max):
                        end = 1
                        break
                        
                if (end == 1):
                    break
                    
            if (end == 1):
                    break
        if (end == 1):
                    break
                    
            
rand = random.randint(0,len(key)-1)
print("YOUR KEY:")
print(key[rand])

