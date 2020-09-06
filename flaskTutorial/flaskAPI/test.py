import requests

base = "http://127.0.0.1:5000/"

#get_resp = requests.get(base + "hello/test")
# get_resp = requests.get(base + "hello")
# post_resp = requests.post(base + "hello")
#print(get_resp.json())
# print(post_resp.json())

# data = [
#     {"likes": 5000, "name": "video 111", "views": 4875},
#     {"likes": 4899, "name": "video 211", "views": 5500},
#     {"likes": 5877, "name": "video 311", "views": 1087},
#     {"likes": 2054, "name": "video 411", "views": 3066},
#     {"likes": 1000, "name": "video 511", "views": 7458}
# ]

# for i in range(len(data)):
#     response = requests.put(base + f"video/{i}", data[i])
#     response = requests.put(base + "video/1", {"likes": 10, "name": "video 1", "views": 1000})
#     print(response.json())
# input()
# response = requests.delete(base + "video/3")
# print(response)
# input()
# response = requests.get(base + "video/10")
# print(response.json())

# - Testing Patch
response = requests.patch(base + "video/2", {'views': 99999, 'likes': 99999})
print(response.json())