from uncertainties import ufloat, ufloat_fromstr
import sys
import argparse
import numpy as np

"""
Enter inputs in the following order:

	1. integrated magnitude within R_eff for the object
	2. uncertainty on the integrated magnitude (0 if no estimate)
	3. effective radius in arcseconds
	4. uncertaintly on the effective radius (0 if no estimate)
	5. axis ratio
	6. uncertainty on axis ratio (0 if no estimate)
	7. Sérsic index
	8. uncertainty on Sérsic index (0 if no estimate)
"""

# m_tot = sys.argv[1] #integrated magnitude within R_eff for object
# m_tot_err = sys.argv[2] #integrated magnitude within R_eff for object
# r_eff = sys.argv[3] #effective radius in arcseconds
# r_eff_err = sys.argv[4] #effective radius in arcseconds
# b_a = sys.argv[5] #axis ratio
# b_a_err= sys.argv[6] #axis ratio
# n = sys.argv[7] #Sérsic index
# n_err= sys.argv[8] #Sérsic index

m = ufloat(float(sys.argv[1]), float(sys.argv[2]))
r = ufloat(float(sys.argv[3]), float(sys.argv[4]))
ba = ufloat(float(sys.argv[5]), float(sys.argv[6]))
n = ufloat(float(sys.argv[7]), float(sys.argv[8]))


def get_mu_eff(m_tot, r_eff, b_a):
	log_term = 2*np.pi*r**2 * ba
	log_err = 0.434 * log_term.s/log_term.n
	return m + 2.5*ufloat(np.log10(log_term.n), log_err)

def get_bn(n): # Ciotti & Bertin (1999) -- https://ui.adsabs.harvard.edu/abs/1999A%26A...352..447C/abstract
	return 2*n - 1/3 + 4/(405*n) + 46/(25515*n**2)

def get_mu0(mu_eff, n):
	"""
	Get central surface brightness assuming a Sérsic index n from the effective surface brightness.
	"""
	return mu_eff - 2.5*get_bn(n)/np.log(10)

print("\n\n")
print("Your effective surface brightness is ", get_mu_eff(m, r, ba))
print("\nand \n")
print("Your central surface brightness is ", get_mu0(get_mu_eff(m, r, ba), n))
print("\n\n")