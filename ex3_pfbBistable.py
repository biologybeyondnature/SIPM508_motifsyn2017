#positive autoregulation with bistability 
import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 65
timePoint = 1000
timeBeginPlot = 0

x1init = np.linspace(0,15,7)

r = te.loada ('''
     # production reactions
     J1: G -> G + X1; a0*G + a*G*(X1^n  / (X1^n + K^n)); 
     
     # degradation reactions
     J3: X1  -> ; b1*X1;

     # set initial condition     
     X1 = 0; G = 1; 

     # production and degradation rate constants
     a = 15.5; a0 = 1;
     b1 = 0.85;  #0.85 default = 0.85 # try 0.9, 0.75

     # association - dissociation rate constant
     K = 10 # larger K means weaker feedback
     n = 2; # Hill co-efficient

 ''')

###################################



###################################

prodX1array = []
degX1array =[]

# probing different initial conditions
for ind in range(0, len(x1init)):
    r.reset()
    x1 = x1init[ind]
    r.X1 = x1
    result = r.simulate(timeBegin, timeEnd, timePoint, ['time','X1','J1','J3'])
    X1timeCourse = result['X1']
    prodX1 = result['J1']
    degX1 = result['J3']
    time = result['time']
    prodX1array.append(prodX1[0])
    degX1array.append(degX1[0])    
    plt.subplot(121)
    plt.plot(time, X1timeCourse)

# running simulation
result_tune = r.simulate(timeBegin, timeEnd, timePoint)
Time_tune = result_tune['time']
X1_tune = result_tune['X1']


#Generate plots
plt.ylabel('[X1]')
plt.xlabel('time')
plt.xlim(timeBeginPlot, timeEnd)
plt.ylim(-0.1, 1.05*x1init[-1])
plt.title('Time Course')

plt.subplot(122)
plt.plot(prodX1array,x1init, color = 'b', label = 'production')
plt.plot(degX1array, x1init, color = 'r', label = 'degradation')
plt.legend(loc = 2)
plt.xlabel('X1 rate of change')
plt.ylim(-0.1, 1.05*x1init[-1])
plt.title('production & degradation function')

plt.show()
