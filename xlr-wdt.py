import xlrd
from xlrd import open_workbook

citycode_path="W:/xx_zd/AMap_adcode_citycode.xlsx/AMap_adcode_citycode.xlsx"
poi_path="W:\\xx_zd\\amap_poicode.xlsx\\高德地图API POI分类编码表.xlsx"

dl=[poi_path,citycode_path]#
dl=[poi_path]#citycode_path


for i in dl:
	data=open_workbook(i)
	if i== citycode_path:
		table=data.sheets()[0]
	else:
		table=data.sheets()[2]
	nr=table.nrows
	nc=table.ncols
	import sys,io 
	sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
	print (nr,nc)

	for i in range(nr):
		for j in range(nc):
			print (table.cell_value(i,j),end=",")
		print ()