import collections;

num = int(input())
D = collections.OrderedDict()

for i in range(num):
    word = input()
    if word in D:
        D[word] +=1
    else:
        D[word] = 1

print(len(D));

for k,v in D.items():
    print(v,end= "");