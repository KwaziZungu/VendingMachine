#kwazi zungu
#Vending machine simulation
#in ZAR


#Methods for calculating and distributing change in rands
def two(change): #For the 2 rands and 1 rands
    div = int(change/2)
    mod = change%2
    if mod==0:
        print('{0} x R2'.format(div))
        return
    else:
        print('{0} x R2\n1 x R{1}'.format(div,mod))
        return
def five(change):
    mod= change%5
    if mod in rands:
        print('1 x R{0}'.format(mod))
    else:
        two(mod)
    print('1 x R5')
    return
def ten(change):
    mod= change%10
    if mod in rands:
        print('1 x R{0}'.format(mod))
    elif mod>5 and mod<10:
        five(mod)
    else:
        two(mod)
    print('1 x R10')
    return
def twenty(change):
    div = int(change/20)
    mod = change%20
    if mod in rands:
        print('1 x R{0}'.format(mod))
    elif mod>10 and mod<20:
        ten(mod)
    elif mod>5 and mod<10:
        five(mod)
    else:
        two(mod)
    print('{0} x R20'.format(div))
    return
def fifty(change):
    mod = change %50
    if mod in rands:
        print('1 x R{0}'.format(mod))
    elif mod>20 and mod<50:
        twenty(mod)
    elif mod>10 and mod<20:
        ten(mod)
    elif mod>5 and mod<10:
        five(mod)
    else:
        two(mod)
    print('1 x R50')
    return
def hundred(change):
    mod = change%100
    if mod in rands:
        print('1 x R{0}'.format(mod))
    elif mod>50 and mod<100:
        fifty(mod)
    elif mod>20 and mod<50:
        twenty(mod)
    elif mod>10 and mod<20:
        ten(mod)
    elif mod>5 and mod<10:
        five(mod)
    else:
        two(mod)
    print('1 x R100')
    return
    

#Machine automation
while True:
    done=False
    rands=[1,2,5,10,20,50,100,200] #Valid ZAR currency coins and bank notes

    try:
        k=float(input('Enter cost(Rands):\n')) #price of object in vending machine

        while not done:
            j=int(input('Deposit ZAR note or coin:\n'))

            #if notes entered are not standard ZAR notes/coins
            if j not in rands:
                print('Invalid deposit')
                continue
            
            #for user to enter valid notes until object is paid for
            while j < k:
                i= int(input('Deposit ZAR note or coin:\n'))
                if i not in rands:
                    print('Invalid deposit')
                    continue
                else:
                    j= j + i

            #if money entered exceeds price... the user should gets their change back of course       
            if j > k:
                change= j-k
                change= round(change,None)
                print('Your change is:')
        
                if change > 2 and change<5 :
                    two(change)
                    done=True
                elif change >5 and change < 10:
                    five(change)
                    done=True
                elif change>10 and change <20:
                    ten(change)
                    done=True
                elif change> 20 and change<50:
                    twenty(change)
                    done=True
                elif change> 50 and change <100:
                    fifty(change)
                    done=True
                elif change>100 and change<200:
                    hundred(change)
                    done=True
                elif change in rands  :
                    print('1 x R{0}'.format(change))
                    done=True
            
            if j == k:
                print('1 x R0')
                done=True
    except ValueError:
        print('Cost not valid!') 
