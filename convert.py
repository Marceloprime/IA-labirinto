import os

def convet(filename):
    f = open(filename,"r")
    file = open("buffer.txt","w")

    f.readline()
    lab = f.read()
    print(lab)
    i = 0
    for i in lab:  
        if(i == '-'):
            print('0', end ="")
            file.write("0")
        elif(i == '\n'):
            print()
            file.write("\n")
        else:
            print("1", end ="")
            file.write("1")    
    f.closed
    file.closed
    return file

def search_char(simb,col,lin,op):
    f = open("teste.txt","r")

    f.readline()
    lab = f.read()
    i = 0
    cont = 1
    x = 1
    y = 0
    for i in lab:  
        if(i == simb):
            break
        elif(i == '\n'):
            continue
        elif(cont == col):
            x = x + 1
            cont = 0 
        cont = cont + 1
    f.closed
    if(op == 'x'):
        return x
    elif(op == 'y'):
        return cont

convet("teste.txt")
print("\n")
print(search_char('$',26,29,'x'))
print(search_char('$',26,29,'y'))
