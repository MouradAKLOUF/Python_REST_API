
#pip install requests
import requests

Base = "http://127.0.0.1:5000/"

#data = [{"name": "Matrix", "likes": 11, "views": 11111},
#    {"name": "DBZ", "likes": 22, "views": 22222},
#    {"name": "Avengers", "likes": 33, "views": 33333}
#    ]

#for i in range(len(data)):
#    response = requests.put(Base + "video/"+str(i) , data[i])
#    print(response.json())

#response = requests.put(Base + "video/1", {"name": "matrix", "likes": 10, "views": 1000})
#print(response.json())

#input()

#response = requests.get(Base + "video/0")
#print(response.json())


#input()

#response = requests.delete(Base + "video/0")
#print(response)

#input()

response = requests.patch(Base + "video/1", {"likes": 99999, "views": 99999})
print(response.json())
response = requests.get(Base + "video/1")
print(response.json())