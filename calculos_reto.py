# By Héctor Miranda García

import math
import numpy as np

w = 115 * 9.81
m = 635
	
# Calculation of values for function "Fx"
	# Calculation of trigonometric functions
fx_t1 = 2 * math.sin(math.radians(60))
fx_t3 = 2 *	math.sin(math.radians(60))
cf = ((0.75 * m) * 9.81)
ct = ((0.25 * m) * 9.81)
# Convertion of function Fx reult
fx_r = - (-cf - ct -w)


#Torque Function values calculation
cf_r1 = (0.8) * cf
ct_r3 = (1.4) * ct

t1_r5 = 2 * 1.55
t2_r7 = -(2 * 2.2)

fy_r = - (-cf_r1 + ct_r3) 

# System of ecuations Matrix
A = np.matrix([[fx_t1, fx_t3],[t1_r5, t2_r7]])
b = np.matrix([[fx_r],[fy_r]])
x = (A**-1)*b # Result

# Printing reults
print("T1 : %s N \nT2 : %s N"%(x[0], x[1]))