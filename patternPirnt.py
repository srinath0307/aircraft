'''#Your code below
n = int(input())
c = n-1
for i in range(n):
    for j in range(n):
        if(i == n//2):
            print(j+1,end = "")
        elif(j == i or j == n-i-1):
            print('*',end = "")
        elif(j == n//2):
            print(i+1,end = "")
        else:
            print('-',end = "")
        c -= 1
    print()'''
''' 
n=int(input())
l=[['-' for j in range(n)] for i in range(n)]
for i in range(n):
    l[i][i]='*'
    l[i][-i-1]='*'
for i in range(1,n+1):
    l[i-1][n//2]=i
    l[n//2][i-1]=i
for i in l:
    print(*i,sep="")
'''

'''
input: 9
'''
'''n=int(input())
val=n
odd=1
for i in range(n):
    print(str(val)*val,end='')
    print('-'*odd,end='')
    print(str(val)*val,end='')
    val-=1
    odd+=2'''



'''
1 2 3 4
5 6 7 8
9 10 11 12
13 14 15 16
'''
'''r,c=map(int,input().split())
matrix=[]
for i in range(r):
    matrix.append(list(map(int,input().split())))
matrix=[list(map(int,input().split())) for i in range(r)]'''


'''from itertools import combinations
test_str="everest"
#res = [test_str[x:y] for x, y in combinations(range(len(test_str) + 1), r = 2)]
res=[]
for i in range(len(test_str)):  #7  ->0,1
    for j in range(i + 1, len(test_str) + 1):  #2,8
        res.append(test_str[i: j])  #1:3
'''

'''s=input().strip()
n=int(input())
s=s*(n//2)
for i in range(n):
    print(s[i],end='')'''

'''s=input().strip()
n=int(input())
l=n//len(s)    
#print(l)
for i in range(l):
    print(s,end='')
l=n%len(s)
#print(l)   
print(s[:l],end='')'''
'''
from tkinter import *
from tkinter import messagebox

root = Tk()
root.title('Tic Tac Toe')

click = True
count = 0


def disablebutton():
    b1.config(state=DISABLED)
    b2.config(state=DISABLED)
    b3.config(state=DISABLED)
    b4.config(state=DISABLED)
    b5.config(state=DISABLED)
    b6.config(state=DISABLED)
    b7.config(state=DISABLED)
    b8.config(state=DISABLED)
    b9.config(state=DISABLED)


def checkifwon():
    global winner
    winner = False

    if b1["text"] == "X" and b2["text"] == "X" and b3["text"] == "X":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    elif b4["text"] == "X" and b5["text"] == "X" and b6["text"] == "X":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    elif b7["text"] == "X" and b8["text"] == "X" and b9["text"] == "X":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    elif b1["text"] == "X" and b4["text"] == "X" and b7["text"] == "X":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    elif b2["text"] == "X" and b5["text"] == "X" and b8["text"] == "X":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    elif b3["text"] == "X" and b6["text"] == "X" and b9["text"] == "X":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    elif b1["text"] == "X" and b5["text"] == "X" and b9["text"] == "X":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    elif b3["text"] == "X" and b5["text"] == "X" and b7["text"] == "X":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "X wins")
        disablebutton()
    # check for O
    elif b1["text"] == "O" and b2["text"] == "O" and b3["text"] == "O":
        b1.config(bg="blue")
        b2.config(bg="blue")
        b3.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()
    elif b4["text"] == "O" and b5["text"] == "O" and b6["text"] == "O":
        b4.config(bg="blue")
        b5.config(bg="blue")
        b6.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()
    elif b7["text"] == "O" and b8["text"] == "O" and b9["text"] == "O":
        b7.config(bg="blue")
        b8.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()
    elif b1["text"] == "O" and b4["text"] == "O" and b7["text"] == "O":
        b1.config(bg="blue")
        b4.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()
    elif b2["text"] == "O" and b5["text"] == "O" and b8["text"] == "O":
        b2.config(bg="blue")
        b5.config(bg="blue")
        b8.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()
    elif b3["text"] == "O" and b6["text"] == "O" and b9["text"] == "O":
        b3.config(bg="blue")
        b6.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()
    elif b1["text"] == "O" and b5["text"] == "O" and b9["text"] == "O":
        b1.config(bg="blue")
        b5.config(bg="blue")
        b9.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()
    elif b3["text"] == "O" and b5["text"] == "O" and b7["text"] == "O":
        b3.config(bg="blue")
        b5.config(bg="blue")
        b7.config(bg="blue")
        winner = True
        messagebox.showinfo("Tic Tac Toe", "O wins")
        disablebutton()

    if count == 9 and winner == False:
        messagebox.showinfo("Tic Tac Toe", "It's a tie")
        disablebutton()


def b_click(b):
    global click, count

    if b["text"] == " " and click == True:
        b["text"] = "X"
        click = False
        count += 1
        checkifwon()
    elif b["text"] == " " and click == False:
        b["text"] = "O"
        click = True
        count += 1
        checkifwon()
    else:
        messagebox.showerror("Tic Tac Toe", "That box has already been selected")


def reset():
    global b1, b2, b3, b4, b5, b6, b7, b8, b9
    global click, count
    click = True
    count = 0
    b1 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b1))
    b2 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b2))
    b3 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b3))
    b4 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b4))
    b5 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b5))
    b6 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b6))
    b7 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b7))
    b8 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b8))
    b9 = Button(root, text=" ", font=("Helvetica", 20), height=3, width=6, bg="SystemButtonFace",
                command=lambda: b_click(b9))
    b1.grid(row=0, column=0)
    b2.grid(row=0, column=1)
    b3.grid(row=0, column=2)
    b4.grid(row=1, column=0)
    b5.grid(row=1, column=1)
    b6.grid(row=1, column=2)
    b7.grid(row=2, column=0)
    b8.grid(row=2, column=1)
    b9.grid(row=2, column=2)


my_menu = Menu(root)
root.config(menu=my_menu)

options = Menu(my_menu, tearoff=False)
my_menu.add_cascade(label="Options", menu=options)
options.add_command(label="Reset Game", command=reset)
reset()
root.mainloop()'''


'''n=int(input())
li=list(map(int,input().split()))
count=0
direction=1
for i in range(n-1):
    if direction%2!=0:
        for j in range(li[i],li[i+1]+1):
            print(j,end=' ')
    else:
        for j in range(li[i+1],li[i]-1,-1):
            print(j,end=' ')
    direction+=1
'''