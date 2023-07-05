# import pandas as pd
#
# from openpyxl import Workbook
# a = Workbook()
# b = a.active
# b["A1"] = "1,2,3,4,5,6,7,8,9,10"
# b.append(["a,b,c,d,e,f,g,h,i,j"])
#
#
# a.save("itstep.xlsx")
# df = pd.read_excel('itstep.xlsx')
#
# a = []
#
# for index, rows in df.iterrows():
#     a.append(rows.to_list())
#
#
#
# from openpyxl import Workbook
# a = Workbook()
# b = a.active
# s = ['a', 'b', 'c', 'd','e', 'f', 'g', 'h', 'i', 'j']
# for i in range(len(s)):
#     print(i, s[i])
#     b.append(s)
#
# a.save("itstep.xlsx")

# from tkinter import *
#
# root = Tk()  # создаем корневой объект - окно
# root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
# root.geometry("300x250")  # устанавливаем размеры окна
# root.colormapwindows()
#
# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
#
# root.mainloop()
# ----------------------------------------------------------------

# import json
#
# j = {
#     "id":1,
#     "nmae":"Jamshid",
#     "age":24,
#     "cars":[
#         {
#         "model":"Tesla","year":2024
#         },
#         {
#           "model":"BMW","year":2020
#         }
#     ]
# }
#
# print(json.dumps(j,indent=4, sort_keys=True))
# indent=4 использует 4 пробела для отступа
# g = json.dumps(j)
# print(g)



# person = '{"id":1,"name":"BOB","languages":["Russion","Uzbek"]}'
# a = json.loads(person)
# print(a['languages'])


# a = """{
#     "people0":{
#          "firstname": "Jumanazar",
#          "LastName":"Jamshid",
#          "age":"Jizzax"
#     },
#     "people2":{
#         "firstName":"Nushafarin",
#         "LastName":"Jumabekova",
#         "age":70,
#         "city":"Andijan"
#     }
#
# }"""


# j = json.loads(a)
# print(j)

# import urllib.request
# import  json
# url = ('https://jsonplaceholder.typicode.com/todos/1')
#
# with urllib.request.urlopen(url) as responce:
#   a = responce.read()
#
# b = json.loads(a)
# user_id = b['userId']
# print(user_id)






# from openpyxl import Workbook
# wb = Workbook()
# ws = wb.active
# treeData = [["STUDENT'S NAME", "COURSE", "BRANCH", "SEMESTER"], ["ANKIT RAI", "B.TECH", "CSE", "4"], ["RAHUL RAI", "M.TECH", "CSE", "2"], ["PRIYA RAI", "MBA", "HR", "3"], ["AISHWARYA", "B.TECH", "CSE", "4"], ["HARSHITA JAISWAL", "B.TECH", "BIOTECH", "5"]]
# for row in treeData:
#     ws.append(row)
#
# wb.save("TreeData.xlsx")



# import json
#
# j = {
#     "id":1,
#     "nmae":"Jamshid",
#     "age":24,
#     "cars":[
#         {
#         "model":"Tesla","year":2024
#         },
#         {
#           "model":"BMW","year":2020
#         }
#     ]
# }
#
# # print(json.dumps(j,indent=4, sort_keys=True))
# # indent=4
# g = json.dumps(j)
# print(g)







# a = """{
#     "people0":{
#          "firstname": "Jumanazar",
#          "LastName":"Jamshid",
#          "age":"Jizzax"
#     },
#     "people2":{
#         "firstName":"Nushafarin",
#         "LastName":"Jumabekova",
#         "age":70,
#         "city":"Andijan"
#     }
#
# }"""
#
# import json
#
# j = json.loads(a)
# print(j)
#
# import urllib.request
# import  json
# url = ('https://jsonplaceholder.typicode.com/todos/1')
#
# with urllib.request.urlopen(url) as responce:
#   a = responce.read()
#
# b = json.loads(a)
# user_id = b['userId']
# print(user_id)


# import requests
# import pandas as pd
# import json
#
# url = 'https://min-api.cryptocompare.com/data/pricemulti?fsyms=BTC,ETH,LUNA,BNB,USDT&amp;tsyms=USD,EUR&amp;api_key={enter-api-key}'
#
# a = requests.request("GET", url)
# b = a.json()
# c = pd.DataFrame(b.items(), columns=['KEY', 'VALUE'])
#
# data_excel = pd.DataFrame(c)
# data_excel.to_excel('currency_rates.xlsx')


# ------------------------------------------------------------------------------



# from tkinter import *
#
# root = Tk()  # создаем корневой объект - окно
# root.title("Приложение на Tkinter")  # устанавливаем заголовок окна
# root.geometry("300x250")  # устанавливаем размеры окна
# root.colormapwindows()
#
# label = Label(text="Hello METANIT.COM")  # создаем текстовую метку
# label.pack()  # размещаем метку в окне
#
# root.mainloop()




# homework
# task 1


# from tkinter import *
#
# root = Tk()
# root.title("Homework")
# root.geometry("270x200")
# root.colormapwindows()
#
#
#
# label = Label(text="", bg="lightgrey", width=30, height=3)
# label.pack()
#
# class Button():
#   btn = Button(width=5, height=2)
#   btn['bg'] = "#ff0000"
#   btn2 = Button(width=5, height=2)
#   btn2['bg'] = "#FFA500"
#   btn3 = Button(width=5, height=2)
#   btn3['bg'] = "#FFFF00"
#   btn4 = Button(width=5, height=2)
#   btn4['bg'] = "#00FF00"
#   btn5 = Button(width=5, height=2)
#   btn5['bg'] = "#87CEEB"
#   btn6 = Button(width=5, height=2)
#   btn6['bg'] = "#0000FF"
#
# Button.btn.pack(side=LEFT)
# Button.btn2.pack(side=LEFT)
# Button.btn3.pack(side=LEFT)
# Button.btn4.pack(side=LEFT)
# Button.btn5.pack(side=LEFT)
# Button.btn6.pack(side=LEFT)
#
#
# def clicked():
#   label.configure(text='siu')


# label.configure(text="Jumanazar najimal knopku")
# x = Button(window, text="Click me", bg="red", command = "clicked")
# x.grid(column=1,row=0)

# root.mainloop()




#
# class Jamshid:
#     def __init__(self,kg):
#         self.kg = kg
#
#     def uz(self):
#         return self.kg * 25
#
#     @property
#     def kg(self):
#         return self.__kg
#     @kg.setter
#
#     def kg(self, new_kg):
#         if isinstance(new_kg, (int, float)):
#             self.__kg = new_kg
#         else:
#             raise ValueError("new_kg daetsa tolko chislo ili drobnoe chislo")
#
# a = Jamshid(10)
# print(a.uz())
# print(a.kg)
# a.kg = 25
# print(a.kg)
#



# class N:
#     n = 17
#     def siu(self):
#      print("cr7 siuuuu")
#
# a=N
# a.siu()

# class B:
#     y = 10
#     def google(self):
#      print(y + 4)

# class Car:
#     pass
# # method
#     def jamshid(self):
#         print("salam jamshid")
#
# a = Car()
# a.jamshid()


class People():
    def __init__(self, NSF, born, phone, city, country, adress):
        self.NSF = NSF
        self.born = born
        self.phone = phone
        self.city = city
        self.country = country
        self.adress = adress