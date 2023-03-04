import turtle
import random
tr=turtle.Turtle()
tr.speed(-1)
tr.width(5)
tr.penup()
tr.goto(-775,410)
z,y=0,-1
def dots():
    l=["red","blue","black","orange","light blue","yellow","purple","magenta","grey","brown","green"]
    tr.pencolor(random.choice(l))
    tr.forward(10)
    tr.pencolor("white")
    tr.forward(10)
arr=[]
row=int(input("enter no of rows of the matrix\n"))
col=int(input("enter no of columns\n"))
rowno=row-1
colno=col-1
if(row/2==0):
    rlim=int(row/2)
else:
    rlim=(row//2)+1
for i in range(rlim):
    for j in range(i,col-i):
       # print(arr[i][j],end=" ")
       if(y==i):
            break
       dots()
       if((i==0)and(j==0)):
           tr.pencolor("white")
           tr.backward(20)
           tr.penup()
           tr.forward(20)
           tr.pendown()
    tr.right(90)
    for k in range(i+1,row-i):
        
        dots()
        #print(arr[k][colno-i],end=" ")
    l=colno-i-1
    tr.right(90)
    while(l>=0+i):
       # print(arr[rowno-i][l],end=" ")
        
        dots()
        l-=1
    m=rowno-i-1
    tr.right(90)
    while(m>=i+1):
        if(z==1):
            break
        dots()
        m-=1
        y=m
     # print(arr[m][0+i],end=" ")
    tr.right(90)
turtle.done()
