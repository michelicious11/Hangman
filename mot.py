# -*- coding: utf-8 -*-
"""
Created on Fri Dec 27 09:11:37 2019

@author: Mick Pl
"""

import random
import xlrd

class Mot:
    def __init__(self, interface):
        self.interface = interface
        
        
    def check_word():
        
    
    def remove_letter():
        
        
    def afficher_letter():
   

    def pick_random_word():
	datapath = '/sdcard/WordDB50.xlsx'
	workbook = xlrd.open_workbook(datapath)
	worksheet = workbook.sheet_by_index(0)
	cell = worksheet.cell(random.randint(1, 50),0)
	return cell
	

