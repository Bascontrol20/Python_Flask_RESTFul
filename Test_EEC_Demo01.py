import requests
API = 'http://localhost:3000/ToteArrivalReport'
'''Requests empty Tote : Storage Plan(Request Tote)'''
# Itemcode = {
#      "ItemCode": "A000001", #Get data D8000(14words) from P'Ya to select Item/When GET data complete move data to D8020 and send M8006 to P'Ya
#      "RequestDateTime":"20210917094450" #Self generate when command operate
# }
# response = requests.get(API,params=Itemcode)
# print(response.text)

'''Requests Picking: Picking Plan'''
# Itemcode = {
#     "OrderNo":"0000001",
#     "ItemCode": "A000001",
#     "CustomerName":"NameCustomer",
#     "RequestDateTime":"20210917094450"

# }
# response = requests.get(API,params=Itemcode)
# print(response.text)

