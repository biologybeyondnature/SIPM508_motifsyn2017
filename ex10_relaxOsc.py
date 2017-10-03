#  This example shows the dynamic of a repressilator

import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 50
timePoint = 1000
timeBeginPlot = 0
timeEndPlot = timeEnd

r = te.loada ('''
     J1: -> X; a1x*(1 + p*X^nx)/(1 + X^nx);
     J2: X -> ; X*bx + g*X*Y;
     J3: -> Y; a1y*(1 + p*X^nx)/(1 + X^nx);
     J4: Y -> ; Y*by; 


     # set parameter     
     X = 10; Y = 0; Z = 0; # initial concentration of protein X, Y
     a1x = 10; a1y = 1; # regulated  production rate of X, Y
     p = 200; # max production regulated by X 
     nx = 4; # Hill's coeff of gene regulation by X
     bx = 0.5; by = 0.5;  # degradation rate of X, Y
     g = 6; # Y catalysed degradation

 ''')

###################################


# running default simulation 
result = r.simulate(timeBegin, timeEnd, timePoint, ['time', 'X','Y','J1'])
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
