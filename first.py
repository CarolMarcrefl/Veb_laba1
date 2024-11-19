print('Введите Xbeg, Xend, Dx и Eps')
xt = float(input('Xbeg = '))
xe = float(input('Xend = '))
dx = float(input('Dx = '))
eps = float(input('Eps = '))
print("+--------+--------+------+")
print("I   X   I   Y   I     N  I")
print("+--------+--------+------+")
x = []
yy = []
N=[]
while xt <= xe:
    an = xt
    n = 0
    y = an
    while True:
        k = -(xt**2)*(2*n+1)/((2*n+2)*(2*n+3)**2)
        an = an * k
        y = y + an
        n = n + 1
        if abs(an) < eps: break
        x += [xt]
        yy += [round(y, 6)]
        N+=[n]
    xt = xt + dx
for i in range(len(x)):
    print("I{0: 7.2f} I{1: 7.3f} I{2: 4} I".format(x[i],yy[i],N[i]))
print("+--------+--------+------+")
