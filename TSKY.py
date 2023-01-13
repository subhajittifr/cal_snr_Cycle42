import sys
import os

#import galacticops as go

def tskypy(freq, gl, gb, tskylist):
    """ Calculate tsky from Haslam table, scale to survey frequency"""
    # ensure l is in range 0 -> 360
    b = gb
    if gl < 0.:
        l = 360 + gl
    else:
        l = gl

    # convert from l and b to list indices
    j = b + 90.5
    if j > 179:
        j = 179

    nl = l - 0.5
    if l < 0.5:
        nl = 359
    i = float(nl) / 4.
    
    tsky_haslam = tskylist[180*int(i) + int(j)]
    # scale temperature before returning
    return tsky_haslam * (freq/408.0)**(-2.6)

def readtskyfile():
    """Read in tsky.ascii into a list from which temps can be retrieved"""

    tskypath = 'tsky.ascii'
    tskylist = []
    with open(tskypath) as f:
        for line in f:
            str_idx = 0
            while str_idx < len(line):
                # each temperature occupies space of 5 chars
                temp_string = line[str_idx:str_idx+5]
                try:
                    tskylist.append(float(temp_string))
                except:
                    pass
                str_idx += 5

    return tskylist
'''
if len(sys.argv)<4:
    print "Supply gl, gb, f_mhz"
    sys.exit()


gl = float(sys.argv[1])
gb = float(sys.argv[2])
f_mhz = float(sys.argv[3])

tskylist = readtskyfile()
print tskypy(f_mhz, gl, gb, tskylist)

'''

