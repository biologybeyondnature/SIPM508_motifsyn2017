#  This example shows how faster production & degradation rates result in faster response of a constitutive gene expression

import tellurium as te
import numpy as np
import pylab as plt

# set simulation time
timeBegin = 0
timeEnd = 25
timePoint = 200
timeBeginPlot = 10
Gval = 1   # concentration of gene
a1val = 1   # production rate constant

r = te.loada ('''
     J1: $G -> $G + X1; a1*G*sw; 
     J2: X1  -> ; b1*X1;

     # set parameter     
     X1 = 0; # initial concentration of gene product
     G = 1; # concentration of gene (DNA template)
     a1 = 1; # production rate
     b1 = 1; # degradation rate

     sw = 0
     at time > 15: sw = 1 # turn on gene expression
     at time > 20: sw = 0 # turn off gene expression 

 ''')

###################################
# default simulation
r.a1 = a1val
r.G = Gval
# running default simulation 
result = r.simulate(timeBegin, timeEnd, timePoint, ['time', 'X1', 'J1'])
# extracting results
Time = result['time']
X1 = result['X1']
J1 = result['J1']
switchState = J1/a1val/Gval  # normalized production rate to get switch state


###################################
## tuned the model to have faster production and degradation rate (sc > 1)
r.reset()
sc = 2
r.a1 = r.a1*sc; r.b1 = r.b1*sc
# running another simulation simulation
result_tune = r.simulate(timeBegin, timeEnd, timePoint)
# extracting result
Time_tune = result_tune['time']
X1_tune = result_tune['X1']

## generate a plot
plt.subplot(211)
plt.plot(Time, X1, color = 'b', label = 'default')    
plt.plot(Time_tune, X1_tune, color = 'r', label = 'tuned')
plt.legend(loc = 'upper right')
plt.ylabel('concentration')
plt.xlim(timeBeginPlot, timeEnd)


plt.subplot(212)
plt.plot(Time, switchState, color = 'k', ls = '--', label = 'input')
plt.xlabel('time')
plt.ylabel('switch state')
plt.xlim(timeBeginPlot, timeEnd)


plt.show()
