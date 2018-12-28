#!/usr/bin/env python3
#unittests.py

import unittest
import os
import glob
import shutil

import numpy as np
from filamentyzer import *

'''
class NameTestCase(unittest.TestCase):
    def test(self):
        name = 'filamentyzer'
        self.assertEqual(filamentyzer.name, name, msg='name should be {}'.format(name))
'''

class IsFilamentyzerTestCase(unittest.TestCase):
    def __init__(self, *args ,**kwargs):
        super().__init__(*args, **kwargs)
        test_path = os.path.dirname(__file__)
        os.chdir(os.path.join(test_path, 'examples'))
        os.makedirs('weak', exist_ok=True)
        os.makedirs('overscaled', exist_ok=True)
        filter_over_weak(glob.glob('*_*.txt'), glob.glob('*_*.png'))

    def test_heat_map(self):
        infile = 'infile'
        data = np.zeros((2, 2), dtype = float)
        plot_heat_map(data, infile)
        self.assertTrue(os.path.isfile(infile + '.png'), msg='plot_heat_map')

    def test_filter_normal(self):
        self.assertTrue(os.path.isfile('norm_norm.txt'), msg='test_filter for normal, txt')
    
    def test_filter_overscaled(self):
        self.assertTrue(os.path.isfile('overscaled/over_over.txt'), msg='test_filter for overscaled, txt')

    def test_filter_weak(self):
        self.assertTrue(os.path.isfile('weak/weak_weak.txt'), msg='test_filter for weak, txt')

    def test_filter_over_png(self):
        self.assertTrue(os.path.isfile('overscaled/name_over_over_name.png'), msg='test_filter for overscaled, png')

    def test_filter_normal_png(self):
        self.assertTrue(os.path.isfile('norm_norm.png'), msg='test_filter for normal, png')

# This function can be used in `setup.py` as `test_suite` keyword argument
def test_suite():
    suite = unittest.defaultTestLoader.loadTestsFromName(__name__)
    return suite

if __name__ == '__main__':  # checks if this file executed as script
    os.chdir('examples')
    filter_over_weak(glob.glob('*_*.txt'), glob.glob('*_*.png'))
    unittest.main()

