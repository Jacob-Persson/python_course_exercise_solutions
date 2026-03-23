# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:45:31 2026

@author: jacpe396
"""

class Birds:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Sparrow', 'Robin', 'Duck']
        
    def printMembers(self):
        print('Printing members of the Birds class')
        for member in self.members:
            print('\t%s ' % member)