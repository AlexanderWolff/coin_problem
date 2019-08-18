''' 
Return Integer value without Decimal Points
'''
def floor(x):
    return int(x-x%1)

''' 
Find value z which fulfills solution y for given multiplier x

y = target value
x = multiplier
i = max value for z
r = reminder
'''
def find_yx_and_r(y, x, i):
    z = ( floor(y/x) if y<x*i else i )
    r = y - z*x
    
    return z, r

'''
Processes through all coin types
'''
def find_change(I, X, y):
    R = [0, 0, 0, 0, 0]
    Y = [0, 0, 0, 0]
    
    R[4] = y  
    for i in [3, 2, 1, 0]:
        Y[i], R[i] = find_yx_and_r(R[i+1], X[i], I[i]) 
    
    if R[0]>0:
        return None
    else:
        return Y
    
'''
Input/Output + Times algorithm
'''
def main():
    from random import randint as r
    import time
    
    # Inventory
    a = r(0,100)
    b = r(0,100)
    c = r(0,100)
    d = r(0,100)
    I = [a, b, c, d]
    print("inventory: 1:{}, 5:{}, 10:{}, 15:{}".format(a,b,c,d))
    
    # Coin types
    xa = 1
    xb = 5
    xc = 10
    xd = 25
    X = [xa, xb, xc, xd]
    
    
    # Input
    try:
        y = int(input('what is initial amount ? : '))
    except:
        print('incorrect input: generating random value')
        y = r(1,300)
    print('change required {0}\n\n'.format(y))


    # Algorithm
    start = time.time()
    s = find_change(I, X, y)
    end = time.time()
    
    
    # Output
    if s==None:
        print("no solution found | in {}s".format(end-start))
    else:
        print('solution: \n\n'
              +'{}x1: \t {} \n'.format(s[0], s[0]*1)
              +'{}x5: \t+{} \n'.format(s[1], s[1]*5)
              +'{}x10: \t+{}\n'.format(s[2], s[2]*10)
              +'{}x25: \t+{}\n'.format(s[3], s[3]*25)
              +'------------\n'
              +'=\t {}\n\n'.format(y)
              +'total coins: {} | calculated in {:.5}s '.format(sum(s), end-start))
    

    

    
    
    









