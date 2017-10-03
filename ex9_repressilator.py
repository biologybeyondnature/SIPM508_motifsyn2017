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
     J1: -> X; a1x*(Kx^nx)/(Kx^nx + Z^nx) + a0x;
     J2: X -> ; X*bx;
     J3: -> Y; a1y*(Ky^ny)/(Ky^ny + X^ny) + a0y;
     J4: Y -> ; Y*by; 
     J5: -> Z; a1z*(Kz^nz)/(Kz^nz + Y^nz) + a0z;
     J6: Z -> ; Z*bz; 

     # set parameter     
     X = 10; Y = 0; Z = 0; # initial concentration of protein X, Y, Z
     a0x = .5; a0y = .5; a0z = .5 # basal production rate of X, Y, Z
     a1x = 216; a1y = 216; a1z = 216; # regulated  production rate of X, Y, Z
     Kx = 1; Ky = 1; Kz = 1; # binding constant at gene X, Y, Z
     nx = 3; ny = 3; nz = 3; # Hill's coeff of gene X, Y, Z regulation
     bx = 1; by = 1; bz = 1 # degradation rate of X, Y, Z

 ''')

###################################


# running default simulation 
result = r.simulate(timeBegin, timeEnd, timePoint, ['time', 'X','Y','Z','J1'])
# extracting results
Time = result['time']
X = result['X']
Y = result['Y']
Z = result['Z']


##############
## generate a plot
plt.subplot(121)
plt.plot(Time, X, color = 'b', label = '[X]')    
plt.plot(Time, Y, color = 'r', label = '[Y]')
plt.plot(Time, Z, color = 'g', label = '[Z]')
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
