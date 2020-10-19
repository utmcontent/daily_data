#encoding=utf-8
from collections import namedtuple
from time import strptime
from re import search,match
from json import dump
import tkinter
# tkinter._test()
from tkinter import *
import datetime
import sys,io
import json
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Rent_C503(object):
	"""docstring for Rent_C503"""
	def __init__(self, date):
		self.date = date
	def main_gui(self):
		parent=Tk()
		parent.resizable(width=False, height=False)
		parent.title("收入支出")
		parent.mainloop()


today=datetime.date.today()
ins_bill=Rent_C503(today)
ins_bill.main_gui()