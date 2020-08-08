import matplotlib.pyplot as p
x=[3,6,8,5,9]
y=[4,7,6,8,2]
p.figure(1)
p.subplot(121)
p.grid()
p.plot(x,y,'r^')
p.subplot(122)
p.plot(x,y,'ro')
p.show()
