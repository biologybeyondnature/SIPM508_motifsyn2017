# genetic switch cascade
import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 100
timePoint = 1000
timeBeginPlot = 30

x1init = np.linspace(0,15,15)

r = te.loada ('''
     # production reactions
     J1: G1 -> G1 + X1; a1*G1; 
     J2: G2 -> G2 + X2; a0*G2 + a*G2*((p*X1^n + q*K^n) / (X1^n + K^n)); 
     J3: G3 -> G3 + X3; a0*G2 + a*G2*((p*X2^n + q*K^n) / (X2^n + K^n)); 
     
     # degradation reactions
     J4: X1  -> ; b1*X1;
     J5: X2  -> ; b1*X2
     J6: X3 -> ; b1*X3;

     # set initial condition     
     X1 = 0; G1 = 1; G2 = 1; G3 = 1; X2 = 0; X3 = 0;

     # production and degradation rate constants
     a1 = 1; b1 = 1; a0 = 1; a = 50;  # try b1 = 0.5, 1, 2

     # association - dissociation rate constant
     K = 40 # larger K means weaker regulation
     n = 1; # Hill co-efficient

     # positive vs negative feedback
     # positive has p = 1 & q = 0; negative has p = 0 & q = 1;
     p = 1; q = 0; 

     # control switch -- alternately switching G1 between production =  1 and 50
     at time > 40: a1 = 50
     at time > 50: a1 = 1
     at time > 80: a1 = 50
     at time > 90: a1 = 1
     
 ''')


result = r.simulate(timeBegin, timeEnd, timePoint, ['time','X1', 'X2', 'X3', 'J1'])
X1 = result['X1']
X2 = result['X2']
X3 = result['X3']
prodX1 = result['J1']
time = result['time']


plt.subplot(211)
plt.plot(time, X1, label = 'X1', color = 'b')
plt.plot(time, X2, label = 'X2', color = 'r')
plt.plot(time, X3, label = 'X3', color = 'g')
plt.legend(loc = 2)
plt.ylabel('conc.')
plt.xlim(timeBeginPlot, timeEnd)
plt.title('Cascade')



plt.subplot(212)
plt.plot(time, prodX1/max(prodX1), color = 'k')
plt.ylabel('switch state')
plt.xlabel('time')
plt.xlim(timeBeginPlot, timeEnd)
plt.show()
