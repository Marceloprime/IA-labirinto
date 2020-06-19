import matplotlib.pyplot as plt
import numpy as np
import queue
import os
import time 

#Author: Marcelo Augusto dos Reis 

class Labyrinth:
    # Attribute

    # Method
    # Initializer with filename as argument
    def __init__(self, filename):
        try:
            f = open(filename, "r")
            lines = f.readlines()
            self.map = np.array([[int(num) for num in line.strip('\n')] for line in lines])
        except FileNotFoundError:
            print("Error, File Not Found")
    
    def setStartAndGoal(self, _start, _goal):
        self.start = _start
        self.goal = _goal

    def validateNode(self, node):
        try:
            return self.map[node[0]][node[1]] == 0
        except IndexError:
            return False

    def AStar(self):
        start_Timer = time.time()
        q = queue.PriorityQueue()
        costSoFar = 0
        distanceToGoal = abs(self.goal[0] - self.start[0]) + abs(self.goal[1] - self.start[1])
        q.put((costSoFar + distanceToGoal, [self.start]))
        goalReached = False
        while not goalReached:
            path = q.get()[1]
            node = path[-1]

            if node == self.goal:
                goalReached = True
                self.path = path
            else:
                costSoFar = len(path) - 1
                #Kanan
                if (node[1] < len(self.map[0]) - 1):
                    if (self.map[node[0]][node[1]+1] == 0) and not [node[0], node[1]+1] in path:
                        optionalNode = [node[0], node[1] + 1]
                        newPath = list(path)
                        newPath.append(optionalNode)
                        #heuristica
                        distanceToGoal = abs(self.goal[0] - optionalNode[0]) + abs(self.goal[1] - optionalNode[1])
                        q.put((costSoFar + distanceToGoal, newPath))
                #Bawah
                if (node[0] < len(self.map) - 1):
                    if (self.map[node[0]+1][node[1]] == 0) and not [node[0]+1, node[1]] in path:
                        optionalNode = [node[0]+1, node[1]]
                        newPath = list(path)
                        newPath.append(optionalNode)
                        distanceToGoal = abs(self.goal[0] - optionalNode[0]) + abs(self.goal[1] - optionalNode[1])
                        #heuristica
                        q.put((costSoFar + distanceToGoal, newPath))
                # Atas
                if (node[0] > 0):
                    if (self.map[node[0]-1][node[1]] == 0) and not [node[0]-1, node[1]] in path:
                        optionalNode = [node[0]-1,node[1]]
                        newPath = list(path)
                        newPath.append(optionalNode)
                        distanceToGoal = abs(self.goal[0] - optionalNode[0]) + abs(self.goal[1] - optionalNode[1])
                        #heuristica
                        q.put((costSoFar + distanceToGoal, newPath))
                #Kiri
                if (node[1] > 0):
                    if (self.map[node[0]][node[1]-1] == 0) and not [node[0], node[1]-1] in path:
                        optionalNode = [node[0], node[1] - 1]
                        newPath = list(path)
                        newPath.append(optionalNode)
                        distanceToGoal = abs(self.goal[0] - optionalNode[0]) + abs(self.goal[1] - optionalNode[1])
                        #heuristica
                        q.put((costSoFar + distanceToGoal, newPath))  
        end_Timer = time.time()
        execTime = end_Timer - start_Timer 
        print(execTime)            

    def BFS(self):
        start_Timer = time.time()
        q = queue.Queue()
        q.put([self.start])
        goalReached = False
        while not goalReached:
            path = q.get()
            node = path[-1]

            if node == self.goal:
                goalReached = True
                self.path = path
            else:
                #Kanan
                if (node[1] < len(self.map[0]) - 1):
                    if (self.map[node[0]][node[1]+1] == 0) and not [node[0], node[1]+1] in path:
                        newPath = list(path)
                        newPath.append([node[0], node[1] + 1])
                        q.put(newPath)
                #Bawah
                if (node[0] < len(self.map) - 1):
                    if (self.map[node[0]+1][node[1]] == 0) and not [node[0]+1, node[1]] in path:
                        newPath = list(path)
                        newPath.append([node[0]+1, node[1]])
                        q.put(newPath)
                #Atas
                if (node[0] > 0):
                    if (self.map[node[0]-1][node[1]] == 0) and not [node[0]-1, node[1]] in path:
                        newPath = list(path)
                        newPath.append([node[0]-1, node[1]])
                        q.put(newPath)
                #Kiri
                if (node[1] > 0):
                    if (self.map[node[0]][node[1]-1] == 0) and not [node[0], node[1]-1] in path:
                        newPath = list(path)
                        newPath.append([node[0], node[1] - 1])
                        q.put(newPath)                
        end_Timer = time.time()
        execTime = end_Timer - start_Timer
        print(execTime)

    def printMap(self):
        plt.close()
        tempMap = self.map.copy()
        try:
            for tile in self.path:
                tempMap[tile[0]][tile[1]] = 2
            self.path = []
        except AttributeError:
            pass

        tempMap[self.start[0]][self.start[1]] = 3
        tempMap[self.goal[0]][self.goal[1]] = 4
        palette = np.array([ [255, 255, 255],
                    [0, 0, 0],
                    [0, 0, 255],
                    [255,0,0],
                    [0,255,0]])
        plt.imshow(palette[tempMap])
        plt.axis("off")
        plt.show(False)

def convet(filename,col):
    f = open(filename,"r")
    file = open("buffer.txt","w")
    string = "buffer.txt"
    f.readline()
    lab = f.read()
    for i in range(col):
        file.write("1")
    file.write("\n")
    i = 0
    for i in lab: 
        if(i == '-'):
            file.write("1")
        elif(i == '\n'):
            file.write("\n")
        else:
            file.write("0") 
    file.write("\n")
    for i in range(col):
        file.write("1")
    f.closed
    file.closed
    return string


#inicio de execucao
if __name__ == "__main__":
    print("Busca em lagura e Busca A*")
    print("Nome do arquivo")
    filename = input()
    while not os.path.isfile(filename):
        print("Error, not found!")
        filename = input()

    print("lin col")
    lin = int(input())
    col = int(input())
    filename = convet(filename,col)
    L = Labyrinth(filename)
    start = list(map(int, input("Posicao incial = ").split(" ")))
    while not L.validateNode(start):
        print("Erro, Posicao incorreta")
        start = list(map(int, input("Posicao incial = ").split(" ")))
    goal = list(map(int, input("Posicao final = ").split(" ")))
    while not L.validateNode(goal):
        print("Erro, Posicao incorreta")
        goal = list(map(int, input("Posicao final = ").split(" ")))
    L.setStartAndGoal(start, goal)
    L.printMap()

    isExit = False

    while not isExit:
        print("Escolha")
        print("1. A*")
        print("2. BFS")
        print("3. Saida")
        method = input(">>")
        if (method.lower() == "a*" or method == '1'):
            L.AStar()
            L.printMap()
        elif (method.lower() == "bfs" or method == '2'):
            L.BFS()
            L.printMap()
        elif (method.lower() == "exit" or method == '3'):
            os.remove("buffer.txt")
            isExit = True
        else:
            print("Comando incorreto")
    