from fake_useragent import UserAgent
from requests import get
import json #解析json数据
import sys,io
import xlrd
# from openpyxl import load_workbook
import os
sys.stdout = io.TextIOWrapper(sys.stdout.buffer,encoding='utf-8')
class GEO(object):
    """docstring for GEO"""
    def __init__(self):
        self.elong,self.nland=111.777844,23.805292#113.460000,22.480000
        self.pagenum=1
        self.citycode_path="AMap_adcode_citycode.xlsx"
        self.url_format="https://restapi.amap.com/v3/place/around?key=6c5e51aa928019b32e0aa4ee51675d0f&location={},{}&radius=1500&types=050000&&sortrule=distance&page={}&extensions=all&output=all"
        self.url=self.url_format.format(self.elong,self.nland,self.pagenum)
        self.fname="geo_near_full_1500.json"#保存文件json格式
        print (self.url)
    def iterate_info(self):#
        with open (self.fname,"r+",encoding="utf-8") as f:
            dict_info=(json.load(f))
        print (len(dict_info["pois"]))
        print (len(set([i["name"] for i in dict_info["pois"]])))
        for i in dict_info["pois"]:
            print (i["name"])
    def update_info(self):
        self.ua = UserAgent()
        self.headers={"user-agent":self.ua.random}
        # assert 1>2
        if "staticimage" in self.url:
            with open("geopic.jpg","wb") as f:
                f.write(t.content)
        elif "050000" in self.url:#编码为美食,各种poi编码在AMap_adcode_citycode.xlsx查看
            t=get(self.url,headers=self.headers)
            dict_geo_data=json.loads(t.text)
            while len(dict_geo_data["pois"])>=1 and self.pagenum<=100:
                if os.path.exists(self.fname):
                    with open (self.fname,"r+",encoding="utf-8") as f:
                        dic_old_data=json.load(f)
                        dic_old_data["pois"].extend(dict_geo_data["pois"])
                    with open (self.fname,"w+",encoding="utf-8") as f:
                        json.dump(dic_old_data,f,ensure_ascii=False)
                else:
                    with open (self.fname,"w+",encoding="utf-8") as f:
                        dic_old_data=dict_geo_data.copy()
                        json.dump(dict_geo_data,f,ensure_ascii=False)
                print ("当前页",self.pagenum)
                self.pagenum+=1
                self.url=self.url_format.format(self.elong,self.nland,self.pagenum)
                t=get(self.url,headers=self.headers)
                dict_geo_data=json.loads(t.text)
                if len(dic_old_data["pois"])>=1000:#数据超过1000就停止自己设置
                    break
if __name__ == '__main__':
    instance=GEO()
    instance.update_info()
    instance.iterate_info()