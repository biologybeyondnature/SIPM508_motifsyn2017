#  This example shows toggle switch

import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 100
timePoint = 1000
timeBeginPlot = 0
timeEndPlot = timeEnd

r = te.loada ('''
     J1: ->  X; a1x*(Kx^nx)/(Kx^nx + ix*Y^nx) + a0x;
     J2: X -> ; X*bx;
     J3: ->  Y; a1y*(Ky^ny)/(Ky^ny + iy*X^ny) + a0y;
     J4: Y -> ; Y*by; 

     # set parameter     
     X = 110; Y = 10; # initial concentration of protein X, Y
     a0x = 10; a0y = 10 # basal production rate of X, Y
     a1x = 100; a1y = 100; # regulated  production rate of X, Y
     Kx = 50; Ky = 50; # binding constant at gene X, Y
     nx = 10; ny = 10;  # Hill's coeff of gene X, Y regulation
     bx = 1; by = 1; # degradation rate of X, y
     ix = 1; iy = 1; # induction by stopping repression at gene X, Y... set to 0 if induced

     at time > 20: iy = 0
     at time > 21: iy = 1
     at time > 40: iy = 0
     at time > 42: iy = 1
     at time > 60: ix = 0
     at time > 61: ix = 1
     at time > 80: ix = 0
     at time > 82: ix = 1

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
#plt.subplot(121)
plt.plot(Time, X, color = 'b', label = '[X]')    
plt.plot(Time, Y, color = 'r', label = '[Y]')
plt.legend(loc = 'upper right')
plt.ylabel('Concentrations')
plt.xlabel('time')
plt.title('Time courses')
plt.xlim(timeBeginPlot, timeEndPlot)



#plt.subplot(122)
#plt.title('Expression trajectories')
#plt.plot(X, Y, color = 'k', ls = '-')
#plt.xlabel('[X]')
#plt.ylabel('[Y]')
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
