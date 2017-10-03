# self-regulatory circuit
import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 120
timePoint = 1000
timeBeginPlot = 30#35
Gval = 1   # concentration of gene
a1val = 50   # production rate constant

x1init = np.linspace(0,15,15)

r = te.loada ('''
     # production reactions
     J1: G -> G + X1; a1*G; 
     J2: G2 -> G2 + X2; a0*G2 + a*G2*((p*X1^n + q*K^n) / (X1^n + K^n)); 
     J3: G3 -> G3 + X3; a0*G2 + a*G2*((p*X2^n + q*K^n) / (X2^n + K^n))*((p*X1^n + q*K^n) / (X1^n + K^n)); 
     
     # degradation reactions
     J4: X1  -> ; b1*X1;
     J5: X2  -> ; b1*X2
     J6: X3 -> ; b1*X3;

     # set initial condition     
     X1 = 0; G = 1; G2 = 1; G3 = 1; X2 = 0; X3 = 0;

     # production and degradation rate constants
     a1 = 1; b1 = .5; a0 = 1; a = 110;

     # association - dissociation rate constant
     K = 80 # larger K means weaker regulation
     n = 2; # Hill co-efficient

     # positive vs negative feedback
     # positive has p = 1 & q = 0; negative has p = 0 & q = 1;
     p = 1; q = 0; 

     # control switch
     at time > 40: a1 = 50
     at time > 70: a1 = 1
     at time > 90: a1 = 50
     at time > 95: a1 = 1
     
 ''')

# play with 


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
plt.title('FFL-C1')



plt.subplot(212)
plt.plot(time, prodX1/max(prodX1), color = 'k')
plt.ylabel('switch state')
plt.xlabel('time')
plt.xlim(timeBeginPlot, timeEnd)
plt.show()
