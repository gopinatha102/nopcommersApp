f = open("text.txt", "r")
list=f.readlines()
for l in list:
    print(l,end="")
