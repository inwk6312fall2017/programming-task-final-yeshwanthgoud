def Words():
    qfile=open('Book1.txt','Book2.txt','Book3.txt','r')
    biggest=''
    for line in qfile:
        if len(line)>len(biggest):
            biggest=line
        return biggest
