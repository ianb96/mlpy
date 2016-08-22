#no symbols math equation
import matplotlib.pyplot as plt
import numpy as np
import random

#gen data
def generate_equation():
    #TODO: make less sequential, less one sided
    #   start with operations and build to left and right?
    #0-plus 1-minus 2-times 3-divide 4-mod #5-exponent
    steps = random.randrange(1,15) 
    #numnumbers = steps+1
    #fullrange = list(range(-99, 0)) + list(range(2, 100))
    fullrange = list(range(-9, 10))
    #fullrange.remove(0)
    #fullrange.remove(1)
    #fullrange.remove(-1)

    nums = [random.choice(fullrange)]#[rand_gauss_nz()]
    equato = nums[0]  
    opers = []
    powlimit = max(2,steps//4)
    numpows = 0
    for s in range(steps):
        nextop = random.randrange(0,6)
        if numpows>=powlimit:
            nextop = random.randrange(0,5)
        nextnum = random.choice(fullrange)#rand_gauss_nz()#
        if nextop == 0:
            equato = equato + nextnum
        elif nextop == 1:
            equato = equato - nextnum
        elif nextop == 2:
            equato = equato * nextnum
        elif nextop == 3:
            brk = 80
            if nextnum==0:
                nextnum+=100 
            while equato % nextnum != 0 and brk>0:
                nextnum = random.choice(fullrange)//2
                #nextnum = rand_gauss_nz()//2
                if nextnum==0:
                    nextnum+100 
                brk-=1
            if brk<=0:
                continue
            equato = equato // nextnum
        elif nextop == 4:
            brk = 20
            while nextnum==0 and brk>0:
                nextnum = random.choice(fullrange)
                brk-=1
            if brk<=0:
                continue
            equato = equato % nextnum
        elif nextop == 5:
            nextnum = random.randrange(1,7)
            equato = equato ** nextnum
            numpows+=1
        else:
            print("range gen error")
        opers.append(nextop)
        nums.append(nextnum)
    while len(str(equato)) >= 10:
        #print("too long!")
        nums, opers, equato = generate_equation()
    #equation = [nums, opers, equato]
    return nums, opers, equato
def rand_gauss_nz():
    n = random.gauss(0, 40)
    if n>=-1:
        n+=3
    return int(n)
opertostr = {0:'+', 1:'-', 2:'*', 3:'/', 4:'%', 5:'^'}
def print_equation(nums, opers, equato):
    [print('(', end='') for _ in range(len(nums)-1)]
    print(nums[0], end='')
    for i in range(len(nums)-1):
        print(opertostr[opers[i]]+''+str(nums[i+1])+')', end='')
    print(' = '+str(equato))


for i in range(100):
    eq = generate_equation()
    #print_equation(eq[0], eq[1], eq[2])
    print([eq[0][i] for i in range(len(eq[0]))], end=',')
    print()
    #print(rand_gauss_nz(),end=',')
# s = rand_gauss_nz()
# #count, bins, ignored = plt.hist(s, 100)
# #plt.plot(bins, np.ones_like(bins), linewidth = 2, color='r')
# ys = [rand_gauss_nz() for i in range(200)]
# plt.bar(ys, [1 for _ in range(100)])
# #plt.scatter(range(100), )
# plt.show()