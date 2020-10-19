#encoding=utf-8
from collections import namedtuple
from time import strptime
from re import search,match
from json import dump
from tkinter import *
import datetime
import sys,io
import json
import os
# sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class Bill_program(object):
	"""docstring for Rent_C503"""
	def __init__(self, date):
		self.date = date
		#初始化你的资产,根据资产类型汇总计算和
		self.type_money_dict={"余额宝":0,"微信零钱":0,"银行卡":0}
		self.count=0
		self.count_list=[]
		self.dayline=[]
		self.cur_a=[]
		with open("my_dict.json","a+") as f:
			f.seek(0)
			dump(self.type_money_dict,f,ensure_ascii=True)
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
		widget3=Button(parent,text="收入",command=lambda:self.saveincome(widget1.get()))
		widget4=Button(parent,text="支出",command=lambda:self.saveoutcome(widget2.get()))
		btn_openoutcome=Button(parent,text="查看支出",command=self.openoutcome)
		btn_openoutcome.grid(row=2,column=1)
		btn_openincome=Button(parent,text="查看收入",command=self.openincome)
		btn_openincome.grid(row=3,column=1)

		widget5_notifiy_money=Label(parent,text="余额1:%.3f"%(self.count),width=28)
		widget6_notifiy_money=Label(parent,text="余额2:%.3f"%(0),width=28)

		day_income=Label(parent,text="日收益:"+str(0),width=40)
		day_out=Label(parent,text="日销预估:"+str(0),width=20)
		widget1.grid(row=0,column=0)
		widget3.grid(row=0,column=1)
		widget2.grid(row=1,column=0)
		widget4.grid(row=1,column=1)
		widget5_notifiy_money.grid(row=4,column=0)
		widget6_notifiy_money.grid(row=5,column=0)
		day_income.grid(row=3,column=0)
		day_out.grid(row=5,column=1)
		parent.mainloop()
	def openincome(self):
		os.system('执行windows cmd程序用sublime打开查看 \"这里要用绝对路径\\你的收入.txt\"')#用notepad 还是 其他文本sublime查看器查看 txt格式的输出
	def openoutcome(self):
		os.system('执行windows cmd程序用sublime打开查看 \"这里要用绝对路径\\你的支出.txt\"')#用notepad 还是 其他文本sublime查看器查看 txt格式的输出
	def saveincome(self,para):#冒号后第一个减号前
		one_e=0
		for el in para.split(" "):
			cell_e=search("\d{1,}",el).group()
			one_e+=float(cell_e)
		with open("你的收入.txt","a+",encoding="utf-8") as f:
			f.write("收入:|"+para+"-"*(45-len(para))+"日期:"+str(self.date)+"\n")
			print ("写入一条 收入|支出 数据")
	def saveoutcome(self,para):
		one_out=0
		for el in para.split(" "):
			cell_out=search("\d{1,}",el).group()
			one_out+=float(cell_out)
		with open("你的支出.txt","a+",encoding="utf-8") as f:
			f.write("支出:|"+para+"-"*(45-len(para))+"日期:"+str(self.date)+"\n")
			print ("写入一条 收入|支出 数据")
	def calculate_value(self,same_depth_list,dep,cur_a):#求dict各项的和
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
if __name__ == '__main__':
	today=datetime.date.today()
	ins_bill=Bill_program(today)
	ins_bill.calculate_value([ins_bill.type_money_dict],0,ins_bill.cur_a)
	ins_bill.main_gui()