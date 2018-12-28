#!/Users/hombit/.virtualenvs/student/bin/python
#test.py
import sys, glob, os
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt
import struct

import filamentyzer
print('Package {} is imported, version is {}'.format(filamentyzer.name, filamentyzer.version))

#setup filenames
path = sys.argv[1]
os.chdir(path)

#analyzer
if (os.path.isdir('weak') == False):
	os.makedirs('weak')
if (os.path.isdir('overscaled') == False):
	os.makedirs('overscaled')
filenames_txt = glob.glob('*_*.txt')
filenames_png = glob.glob('*_*.png')

filamentyzer.filter_over_weak(filenames_txt, filenames_png)

