import numpy as np
import matplotlib.pyplot as plt

data_b3 = np.loadtxt('band3.par')
data_b5 = np.loadtxt('band5.par')


def g_by_t_sys(data, nu):
	exponents = data[:,1]
	coeff = data[:,0]
	nos = len(exponents)
	g_b_t =0.0
	for k in range(nos):
		power = k
		g_b_t = g_b_t + (coeff[k]*10.**exponents[k])*nu**(float(k))
	return g_b_t

'''	
nu_array = np.linspace(260, 500, 1000)
g_by_tsys =[]
for i in nu_array:
	g_by_tsys.append(g_by_t_sys(data_b3, i))
	
plt.plot(nu_array, np.array(g_by_tsys)*1000., color='k', linewidth=2.5)
plt.title('BAND-3')
plt.xlabel('Frequency (MHz)')
plt.ylabel(r'1000$\times$G/T$_{sys}$ (Jy $^{-1}$)')
plt.grid()
#plt.show()
plt.savefig('BAND3.pdf')
'''
