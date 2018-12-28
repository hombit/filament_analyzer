#!/usr/bin/env python3
#f_a.py
"""
An analyzer module: \
filter for overscaled and weak images \
"""

import sys, glob, os
import numpy as np
import scipy as sp
import matplotlib as mpl
import matplotlib.pyplot as plt

def filter_over_weak(filenames_txt, filenames_png):
	"""
	This function filters images: normal, overscaled and weak 
	and then plots 2d heat maps if they don't exist.
	"""
	#params setting
	MAX_VAL = 1022	
	print(filenames_txt)

	#read data
	for filename in filenames_txt:
		data = np.loadtxt(filename)

		print("filter: " + filename + ' is processing')
		f_name = filename.split(".txt")[0]
		f_params = f_name.split('_')[:]
		img_exist = 0

		x_max, y_max = np.unravel_index(np.argmax(data), data.shape)

		#let's filter overscaled and weak
		if (data[x_max, y_max] > MAX_VAL):
			os.rename(filename, 'overscaled/' + filename)
			
			for f_n in filenames_png:
				f_name_png = f_n.split(".png")[0]
				f_png_params = f_name_png.split('_')[:]
				if (f_png_params[1:3] == f_params[0:2]):
					os.rename(f_n, 'overscaled/' + f_n)
					img_exist = 1
					break
			if (img_exist == 0):		
				plot_heat_map(data, "overscaled/" + f_name)	
		else:
			s = 0.0
			for i in range(x_max-1, x_max+2):
				for j in range(y_max-1, y_max+2):
					if (i != x_max or j != y_max):
						s += data[i,j]
			
			if (data[x_max, y_max] > s/4.0):
				os.rename(filename, 'weak/' + filename)
				for f_n in filenames_png:
					f_name_png = f_n.split(".png")[0]
					f_png_params = f_name_png.split('_')[:]
					if (f_png_params[1:3] == f_params[0:2]):
						os.rename(f_n, "weak/" + f_n)
						img_exist = 1
						break
				if (img_exist == 0):		
					plot_heat_map(data, "weak/" + f_name)	

			else:
				for f_n in filenames_png:
					f_name_png = f_n.split(".png")[0]
					f_png_params = f_name_png.split('_')[:]
					if (f_png_params[1:3] == f_params[0:2]):
						img_exist = 1
						break		
				if (img_exist == 0):		
					plot_heat_map(data, f_name)		

def plot_heat_map(data, filename):
	"""
	This function plots heat maps of data nupmy 2d array and save result to filename.png.
	"""
	#heat map plotting
	plt.xlabel(r'$x$')
	plt.ylabel(r'$y$')
	plt.grid(True)
	plt.minorticks_on()
	plt.tick_params(axis='x', pad=7)
	plt.tick_params(axis='y', pad=5)

	plt.imshow(data, cmap='magma', interpolation='nearest')
	plt.colorbar()
	plt.savefig(filename + ".png", bbox_inches='tight')

	plt.close()
	
