'''
816
357
492
'''
import itertools
from tkinter import *
import random
#import time
#todo: machine learning for ai


root = Tk()

lab = Label(root, text="Player 1's turn")
entr = Entry(root)
buts = [Button(root, text=str(i+1), borderwidth=4, padx=10, pady=10, font=("",50), disabledforeground="#fff") for i in range(9)]
#, command=lambda: pinput((i+1)) doesnt work all->9

buts[0]['command']=lambda :pinput(1)
buts[1]['command']=lambda :pinput(2)
buts[2]['command']=lambda :pinput(3)
buts[3]['command']=lambda :pinput(4)
buts[4]['command']=lambda :pinput(5)
buts[5]['command']=lambda :pinput(6)
buts[6]['command']=lambda :pinput(7)
buts[7]['command']=lambda :pinput(8)
buts[8]['command']=lambda :pinput(9)

lab.grid(row=3,column=0)
#entr.grid(row=3, column=3)
buts[7].grid(row=0, column=0)
buts[0].grid(row=0, column=1)
buts[5].grid(row=0, column=2)
buts[2].grid(row=1, column=0)
buts[4].grid(row=1, column=1)
buts[6].grid(row=1, column=2)
buts[3].grid(row=2, column=0)
buts[8].grid(row=2, column=1)
buts[1].grid(row=2, column=2)

# buts[7].grid(column=0, row=0)
# buts[0].grid(column=1, row=0)
# buts[5].grid(column=2, row=0)
# buts[2].grid(column=3, row=0)
# buts[4].grid(column=4, row=0)
# buts[6].grid(column=5, row=0)
# buts[3].grid(column=6, row=0)
# buts[8].grid(column=7, row=0)
# buts[1].grid(column=8, row=0)


root.wm_title("3 numbers to 15")
print("Get to 15!")
turn = 1
numplayers = 2
wincount = [0,0]
print(numplayers, "players")
over=False
pls = [[],[]]
redcol="#f55"
bluecol="#55f"
redwincol="#f22"
bluewincol="#22f"
defcol=buts[0].cget("background")
#b = [0 for _ in range(9)]

# def keycall(event):
#     pass
# frame = Frame(root, width=100, height=100)
# frame.bind("<Key>", keycall)
# frame.pack()

def reset():
    global pls, turn, over
    over=False
    pls = [[],[]]
    if turn == 1:
        turn = 2
    else:
        turn = 1
    for but in buts:
        but['state']=NORMAL
        but['background']=defcol
    lab.config(text="Player "+str(turn)+"'s turn")
    print("--reset--\n")
    print("first turn: p"+str(turn))

#if any three numbers adds up to 15 return true 
def won(pl):
    global over
    if len(pl)>=3:
        for p in itertools.permutations(pl, 3):
            if sum(p) == 15:
                over=True
                return True, p
    #check tie
    if len(pl)>=4:
        if len(pls[0])+len(pls[1])==9:
            print("tie")
            reset()
    return False, 0

#go to the next turn
def nextturn():
    global turn
    if turn == 1:
        turn = 2
        #print("turn:", turn)
        if numplayers == 2:
            #next player
            lab.config(text="Player 2's turn")
            pass
        else:
            #ai turn
            lab.config(text="ai turn")
            aiplay()
    else:
        turn = 1
        #print("turn:", turn)
        if numplayers == 0:
            #ai turn
            lab.config(text="ai turn")
            aiplay()
        else:
            #next players turn
            lab.config(text="Player 1's turn")
            pass
    
#display win hold, and reset
def wingame(poss):
    print("p"+str(turn), "won")
    wincount[turn-1]+=1
    lab['text']="Player "+str(turn)+" won!"#in a function?  
    for ps in poss:
        if turn == 1:
            buts[ps-1]['background'] = redwincol
        else:
            buts[ps-1]['background'] = bluewincol
    #wait and reset
    root.after(3000, lambda:reset())
    print("wins: \np1:", wincount[0], " p2:", wincount[1])

#player input
def pinput(num):
    if over:
        return
    print("p"+str(turn),"selected",num)
    if turn <= numplayers:
        h=num-1
        if buts[h]['state']!=DISABLED:
            if turn == 1:
                buts[h]['background']=redcol
            else:
                buts[h]['background']=bluecol
            buts[h]['state']=DISABLED
            pls[turn-1].append(num)
            win, winposs = won(pls[turn-1])
            #buts[h].after(10)
            if win:
                wingame(winposs)
                return
            #print("pfinish")
            nextturn()
        else:
            #cannot go there
            print("cannot go there")
            pass 

#ai turn
def aiplay():
    #svm?
    #machine learning hopefully
    #is even possible?
    #not recommended for sure
    #add function for learning?


    pinput(random.randrange(1,10))
    print("aifinish")
    #nextturn()
    pass



root.mainloop()
