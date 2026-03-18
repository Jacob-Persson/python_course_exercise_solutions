# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:55:35 2026

@author: jacpe396
"""

# -*- coding: utf-8 -*-
"""
Created on Tue Mar 17 11:45:57 2026

@author: jacpe396
"""

class Fish:
    def __init__(self):
        ''' Constructor for this class. '''
        # Create some member animals
        self.members = ['Salmon', 'Tuna', 'Goldfish']
    
    def printMembers(self):
        print('Printing members of the Fish class')
        for member in self.members:
            print('\t%s ' % member)
