import requests
API = 'http://localhost:3000/mettings'
'''For GET requests'''
# data = {
#     "id" : 2 ,

# }

# response = requests.get(API,params=data)
# print(response.text)

'''For POST Requests'''
# data = {
#     "id" : 7,
#     "title" : "Plan7",
#     "day" : "Monday"

# }

# response = requests.post(API,data=data)
# print(response.text)
'''For PUT Requests'''
data = {
    "id" : 3,
    "title" : "Facebook Update!!!",
    "day" : "Saturday!!!"

}
id=3
response = requests.put(API + '/'+str(id),data=data)
print(response.text)

'''For DELETE Requests'''
# id = 2
# response = requests.delete(API + '/'+str(id))
# print(response.text)


'''For Testing print data'''
#print(response.status_code) #200
#print(response.json())
''' [{'id': 1, 'title': 'Google Meet', 'day': 'Monday'}, {'id': 2, 'title': 'Twiiter', 'day': 'Tueday'}, {'id': 3, 'title': 'Facebook', 'day': 'Wednesday'}, {'id': 4, 'title': 'Amazon', 'day': 'Thursday'}, {'id': 5, 'title': 'Tesla', 'day': 'Friday'}]'''

#print(response.content)
'''b'[\n  {\n    "id": 1,\n    "title": "Google Meet",\n    "day": "Monday"\n  },\n  {\n    "id": 2,\n    "title": "Twiiter",\n    "day": "Tueday"\n  },\n  {\n    "id": 3,\n    "title": "Facebook",\n    "day": "Wednesday"\n  },\n  {\n    "id": 4,\n    "title": "Amazon",\n    "day": "Thursday"\n  },\n  {\n    "id": 5,\n    "title": "Tesla",\n    "day": "Friday"\n  }\n]'''

#print(response.text)
'''
[
  {
    "id": 1,
    "title": "Google Meet",
    "day": "Monday"        
  },
  {
    "id": 2,
    "title": "Twiiter",    
    "day": "Tueday"        
  },
  {
    "id": 3,
    "title": "Facebook",
    "day": "Wednesday"
  },
  {
    "id": 4,
    "title": "Amazon",
    "day": "Thursday"
  },
  {
    "id": 5,
    "title": "Tesla",
    "day": "Friday"
  }
]
'''