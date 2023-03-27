from graphics import *
import random
import math


def in_square(pointer, square):
    inside_square=False
    corner_a=square.getP1()
    corner_b=square.getP2()
    
    if (pointer.getX()>=corner_a.getX() and pointer.getX()<=corner_b.getX()):
        if (pointer.getY()>=corner_a.getY() and pointer.getY()<=corner_b.getY()):
            inside_square=True
    return inside_square

def main(size):
    
    window=GraphWin("Nolan's paradise", size*90, size*90)
    list_squares=[]
    list_status_square=[]
    
    for y in range(size):
        tmp_list=[]
        tmp_status=[]
        for x in range(size):
            status=-1
            window.plot(x*90, y*90, "yellow")
            rect=Rectangle(Point(x*90, y*90), Point((x+1)*90, (y+1)*90))
            if ((random.randint(0, 100))%2==0):
                rect.setFill("yellow")
                status=0
            else:
                rect.setFill("green")
                status=1
            tmp_list.append(rect)
            tmp_status.append(status)
        list_squares.append(tmp_list)
        list_status_square.append(tmp_status)
    
    
    for row in list_squares:
        for rect in row:
            rect.draw(window)
    
    while True:
        mouse=window.getMouse()
        for row in list_squares:
            for rect in row:
                if in_square(mouse, rect):
                    print(list_squares.index(row), row.index(rect), list_status_square[list_squares.index(row)][row.index(rect)])
                    if list_status_square[list_squares.index(row)][row.index(rect)]==0:
                        
                        rect.setFill("green")
                        list_status_square[list_squares.index(row)][row.index(rect)]=1
                    else:
                        rect.setFill("yellow")
                        list_status_square[list_squares.index(row)][row.index(rect)]=0
                    
                    
                    if (row.index(rect)-1>=0):
                        if (list_status_square[list_squares.index(row)][row.index(rect)-1]==0):
                            row[row.index(rect)-1].setFill("green")
                            list_status_square[list_squares.index(row)][row.index(rect)-1]=1
                        else:
                            row[row.index(rect)-1].setFill("yellow")
                            list_status_square[list_squares.index(row)][row.index(rect)-1]=0
                    
                    if (row.index(rect)+1<=-1+size):
                        if (list_status_square[list_squares.index(row)][row.index(rect)+1]==0):
                            row[row.index(rect)+1].setFill("green")
                            list_status_square[list_squares.index(row)][row.index(rect)+1]=1
                        else:
                            row[row.index(rect)+1].setFill("yellow")
                            list_status_square[list_squares.index(row)][row.index(rect)+1]=0
                    
                    if (list_squares.index(row)-1>=0):
                        if (list_status_square[list_squares.index(row)-1][row.index(rect)]==0):
                            list_squares[list_squares.index(row)-1][row.index(rect)].setFill("green")
                            list_status_square[list_squares.index(row)-1][row.index(rect)]=1
                        else:
                            list_squares[list_squares.index(row)-1][row.index(rect)].setFill("yellow")
                            list_status_square[list_squares.index(row)-1][row.index(rect)]=0
                    
                    if (list_squares.index(row)+1<=-1+size):
                        if (list_status_square[list_squares.index(row)+1][row.index(rect)]==0):
                            list_squares[list_squares.index(row)+1][row.index(rect)].setFill("green")
                            list_status_square[list_squares.index(row)+1][row.index(rect)]=1
                        else:
                            list_squares[list_squares.index(row)+1][row.index(rect)].setFill("yellow")
                            list_status_square[list_squares.index(row)+1][row.index(rect)]=0
    
    window.getMouse()
    
size=int(input())
main(size)

