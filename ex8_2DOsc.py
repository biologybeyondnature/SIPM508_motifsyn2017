#  This example shows 2D damped oscillator

import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 10
timePoint = 1000
timeBeginPlot = 0
timeEndPlot = timeEnd

r = te.loada ('''
     J1: ->  X; a1x*(Kx^nx)/(Kx^nx + Y^nx) + a0x;
     J2: X -> ; X*bx;
     J3: ->  Y; a1y*(X^ny)/(Ky^ny + X^ny) + a0y;
     J4: Y -> ; Y*by; 

     # set parameter     
     X = 100; # initial concentration of protein X
     Y = 0; # initial concentration of protein Y
     a0x = 10; # basal production rate of X
     a0y = 10; # basal production rate of Y
     a1x = 100; # regulated  production rate of X
     a1y = 100; # regulated  production rate of Y
     Kx = 50; # binding constant at gene X
     Ky = 50; # binding constatn at gene Y
     nx = 10; # Hill's coeff of gene X regulation
     ny = 10; # Hill's coeff of gene Y regulation
     bx = 1; # degradation rate of X
     by = 1; # degradation rate of Y

 ''')

###################################


# running default simulation 
result = r.simulate(timeBegin, timeEnd, timePoint, ['time', 'X', 'Y', 'J1'])
# extracting results
Time = result['time']
X = result['X']
Y = result['Y']


##############
## generate a plot
plt.subplot(121)
plt.plot(Time, X, color = 'b', label = '[X]')    
plt.plot(Time, Y, color = 'r', label = '[Y]')
plt.legend(loc = 'upper right')
plt.ylabel('Concentrations')
plt.xlabel('time')
plt.title('Time courses')
plt.xlim(timeBeginPlot, timeEndPlot)



plt.subplot(122)
plt.title('Expression trajectories')
plt.plot(X, Y, color = 'k', ls = '-')
plt.xlabel('[X]')
plt.ylabel('[Y]')
#plt.xlim(timeBeginPlot, timeEnd)

#######################
# set axis limit
#plt.ylim(-0.1, 1.5)
#plt.xlim(-0.1, 10)

print("X:---------")
print(X)
print("Y:---------")
print(Y)

plt.show()
