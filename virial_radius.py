
import sys
import astropy.units as u

mass = float(sys.argv[1]) * u.Msun

#### Mowla et al. 2019 ####

r_p = 8.6*u.kpc
M_p = 10**10.2*u.Msun
a = 0.17
b = 0.50
d = 6

r_80 = r_p * (mass/M_p)**a * ((1/2)*(1 + (mass/M_p)**d))**((b-a)/d)

r_vir = r_80/0.047


print('\n\n')
print('For stellar mass %.1E Msun, the virial radius is %.2f kpc.'%(mass.value, r_vir.value))
print('\n')