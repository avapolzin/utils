from astropy.coordinates import SkyCoord
import sys

ra_in = sys.argv[1]
dec_in = sys.argv[2]

coord = SkyCoord(ra_in, dec_in, unit = 'deg')

ra_hr = int(coord.ra.hour)
ra_min = int((coord.ra.hour - int(coord.ra.hour))*60)
ra_sec = ((coord.ra.hour - int(coord.ra.hour))*60 - int((coord.ra.hour - int(coord.ra.hour))*60))*60

dec_out = str(coord.dec).replace('d', ':').replace('m', ':').replace('s', '')

print('%i:%i:%.1f %s'%(ra_hr, ra_min, ra_sec, dec_out)) #RA precision based on DF images, could be changed later