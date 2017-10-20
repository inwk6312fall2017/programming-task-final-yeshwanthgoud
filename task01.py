my_f1 = ("Book1.txt")
my_f2 = ("Book2.txt")
my_f3 = ("Book3.txt")

def Words():
    qfile=open('my_f1','my_f2','my_f3','r')
    biggest=''
    for line in qfile:
        if len(line)>len(biggest):
            biggest=line
        return biggest
print (words)

