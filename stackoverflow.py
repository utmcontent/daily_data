#encoding=utf-8
from collections import namedtuple
from time import strptime
from re import search,match
from json import dumpimport tkinter
tkinter._test()
from tkinter import *
import datetime
import sys,io
import json
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')

class Rent_C503(object):
	"""docstring for Rent_C503"""
	def __init__(self, date):
		self.date = date
		self.mango={"ab":0,"ac":0,"ad":0,"ae":{"af":0},"ag":0,"ah":0,"ai":0,"aj":0,"ak":{"al":-584.85,"am":0.0},"an":{"ao":-315.61,"ap":0},"aq":-807.67,"ar":0,"as":0,"at":-6500,"au":0,"av":0,"aw":10}#"房产":1e6+1e5#+230.05-230.05
		self.count=0
		self.count_list=[]
		self.dayline=[]
		self.cur_a=[]
		# with open("my_block_ch.json","a+") as f:
		# 	f.seek(0)
		# 	dump(self.mango,f,ensure_ascii=True)
		#self.cost=namedtuple("sum_cost","")
	def main_gui(self):
		parent=Tk()
		parent.resizable(width=False, height=False)
		parent.title("收入支出")
		income,outcome=StringVar(),StringVar()
		Menu(parent)
		date_label=Label(parent,text=self.date,width=26)
		date_label.grid(row=2,column=0)
		widget1=Entry(parent,textvariable=income,width=26)
		widget2=Entry(parent,textvariable=outcome,width=26)
		widget3=Button(parent,text="income submit",command=lambda:self.saveincome(widget1.get()))
		widget4=Button(parent,text="outcome submit",command=lambda:self.saveoutcome(widget2.get()))
		btn_openoutcome=Button(parent,text="view income",command=self.openoutcome)
		btn_openoutcome.grid(row=2,column=1)
		btn_openincome=Button(parent,text="view outcome",command=self.openincome)
		btn_openincome.grid(row=3,column=1)

		widget5_notifiy_money=Label(parent,text="left:%.3f"%(self.count),width=28)
		widget6_notifiy_money=Label(parent,text="remain:%.3f"%(0000000),width=28)

		day_income=Label(parent,text="日收益:"+str(0),width=40)
		day_out=Label(parent,text="日销预估():"+str(50),width=20)
		widget1.grid(row=0,column=0)
		widget3.grid(row=0,column=1)
		widget2.grid(row=1,column=0)
		widget4.grid(row=1,column=1)
		widget5_notifiy_money.grid(row=4,column=0)
		widget6_notifiy_money.grid(row=5,column=0)
		day_income.grid(row=3,column=0)
		day_out.grid(row=6,column=1)
		parent.mainloop()
	def openincome(self):
		import os
		os.system('start \"\" \"C:\\zd_bc_xp_zd\\Sublime Text 3\\sublime_text.exe\" \"W:\\cl\\moneyis_infoenv_one\\income.txt\"')
	def openoutcome(self):
		import os
		os.system('start \"\" \"C:\\zd_bc_xp_zd\\Sublime Text 3\\sublime_text.exe\" \"W:\\cl\\moneyis_infoenv_one\\outcome.txt\"')
	def saveincome(self,para):#冒号后第一个减号前
		one_e=0
		for el in para.split(" "):
			cell_e=search("\d{1,}",el).group()
			one_e+=float(cell_e)
		with open("W:\\cl\\moneyis_infoenv_one\\income.txt","a+",encoding="utf-8") as f:
			f.write("收入:|"+para+"-"*(45-len(para))+"日期:"+str(self.date)+"\n")
			print ("write a income")
	def saveoutcome(self,para):
		one_out=0
		for el in para.split(" "):
			cell_out=search("\d{1,}",el).group()
			one_out+=float(cell_out)
		with open("W:\\cl\\moneyis_infoenv_one\\outcome.txt","a+",encoding="utf-8") as f:
			f.write("支出:|"+para+"-"*(45-len(para))+"日期:"+str(self.date)+"\n")
			print ("write a outcome")
	def calculate_value(self,same_depth_list,dep,cur_a):
		if not same_depth_list:
			return
		for el_list in same_depth_list:
			for sub_el in el_list:
				if type(el_list[sub_el]) in (float,int):
					value=el_list[sub_el]
					self.count+=value
					self.count_list.append(value)
				if type(el_list[sub_el])==dict and len(el_list[sub_el])>0:
					cur_a.append(el_list[sub_el])
		print (cur_a)
		self.calculate_value(cur_a,dep+1,[])
	def estimate_yearcost(self):
		t=["0."+str(i) for i in range(51,117) if i<100]#insert into right place
		s=[float(i) for i in t]
		print ("cost:",9*365+100*12+30*12+4*365+13*10+10*180+10*365)


today=datetime.date.today()
ins_bill=Rent_C503(today)
ins_bill.calculate_value([ins_bill.mango],0,ins_bill.cur_a)
ins_bill.main_gui()