# import numpy as np
# print(dir(np))

# d1 = np.array([101,102,103])
# d2 = np.array([[1,2,3],[4,5,6],[16,7,8],[9,10,11]])
# d3 = np.array([[[1,2,3],[4,5,6],[6,7,8],[9,10,11]],[[12,22,32],[42,52,62],[62,72,82],[92,102,112]]])
# arr = np.array([1, 2, 3, 4], ndmin=5)
# print(arr)
# print(d1,d1.ndim)
# print(d2,d2.ndim)
# print(d3,d3.ndim)

# # print(d1[2])
# print(d2[1][2])
# print(d3[1][2][2])

# print(d1[1:])
# print(d1[:])
# print(d2[2:])
# print(d2[::-1])
# print(d3[1:])
# print(d3[1:2])


# arrc = np.array([1,2,3,4,5])
# x1 = arrc.copy()
# arrc[0] = 22
# print(arrc)
# print(x1)

# arrv = np.array([1,2,3,4,5])
# x2 = arrv.view()
# arrv[0] = 22
# print(arrv)
# print(x2)

# shapping = np.array([11,22,33,54], ndmin=5)
# print(shapping)
# print('shape of array :', shapping.shape)

# reshapee = np.array([1,2,3,4,5,6,7,8,9,10,11,12])
# print(reshapee)
# print("reshape =",reshapee.reshape(2,6))

# iter = np.array([[1,2,3],[4,5,6]])
# for i in iter:
#     for j in i:
#         print(j,end=" ")

# arr1 = np.array([[[1, 2], [3, 4]], [[5, 6], [7, 8]]])
# for x in np.nditer(arr1):
#   print(x,end=" ")

# arr11 = np.array([[1, 2], [3, 4]])
# arr22 = np.array([[5, 6], [7, 8]])
# conarr = np.concatenate((arr11, arr22))
# conarraxis = np.concatenate((arr11, arr22),axis=1)
# print(conarr)
# print(conarraxis)

# searcharr = np.array([1, 2, 3, 4, 5, 4, 4])
# x = np.where(searcharr == 4)
# print(x)

# add1 = np.array([[1,2,3],[4,5,6]])
# add2 = np.array([1,1,1])
# print(add1 + add2)

# ======================PANDAS=========================

# import pandas as pd
# print(dir(pd))
# data1 = pd.DataFrame()
# data2 = pd.DataFrame([11,22,33,44,55])
# data3 = pd.DataFrame([["likhitha",23,"MCA"],["Poojitha",19,"B.Pharm"]])
# print(data1)
# print(data2)
# print(data3)

# dataset = [["likhitha",23,"MCA"],["Poojitha",19,"B.Pharm"],["kavitha",45,"7th"],["sathish",54,"4th"]]
# data4 = pd.DataFrame(dataset,columns=["name","age","study"])
# print(data4)

# data5 = pd.DataFrame(dataset,columns=["name","age","study"],index=["student1","student2","student3","student4"])
# print(data5)
# print(data5.head(2))
# print(data5.tail(2))
# print(data5.tail(3))
# print(data5.sum())
# print(data5.sum(1))
# print(data5.max())
# print(data5.min())
# print(data5.count())

# seriess = {
#     "sugar" : 120,
#     "salt" : 20,
#     "tea powder" : 50
# }
# mydata = pd.Series(seriess,index=[1,2,3]) #error
# mydata = pd.Series(seriess,index=["sugar"])
# print(mydata)

# csvdataa = pd.read_csv("student.csv")
# print(csvdataa)
# print(pd.options.display.max_rows) #60
# pd.options.display.max_rows = 9999
# print(pd.options.display.max_rows) #9999

# import csv
# newrow = ["ammu" , 24 , "india" , 5000]
# with open("student.csv","a",newline='') as f:
#     writing = csv.writer(f)
#     writing.writerow(newrow)
#     print("row added successfully")

# import json
# with open("student.json","r") as f:
#     data = json.load(f)
# print(data)
    
# import json
# student = {
#     "name": "Likhitha",
#     "age": 21,
#     "city": "Hyderabad"
# }
# with open('student.json', 'w') as file:
#     json.dump(student, file)

# import requests
# data = requests.get("https://fakestoreapi.com/products")
# print(data.status_code)      
# # print(data.json())       
# data_list = data.json()
# for i in data_list:
#     for j in i:
#         if j == "title":
#             print(i["title"])

# import requests
# url = "https://jsonplaceholder.typicode.com/posts"
# data = {
#     "userId": "3",
#     "title": "nothing",
#     "body": "something"
# }
# dictdata = [
#     {
#         "userId": "1",
#         "title": "womens",
#         "body": "womens wear"
#         },
#     {
#         "userId": "2",
#         "title": "mens",
#         "body": "menswear"
#         }

# ]
# newdata = requests.post(url,json=data)
# newdata2 = requests.post(url,json=dictdata)

# newdatalist = newdata.json()
# newdatalist2 = newdata2.json()

# print(newdatalist)
# print(newdatalist2)



