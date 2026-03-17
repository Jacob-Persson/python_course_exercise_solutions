# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:45:57 2026

@author: jacpe396
"""

class Mammals:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Tiger', 'Elephant', 'Wild cat']
    
    def printMembers(self):
        print('Printing members of the Mammals class')
        for member in self.members:
            print('\t%s ' % member)
