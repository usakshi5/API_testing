import requests
import payload

url = 'http://216.10.245.166/Library/Addbook.php'

add_response = requests.post(url, json = payload.add_book_data, headers = {'Content-Type': 'application/json'} )
json_response = add_response.json()
print(json_response)
print(add_response.status_code)
id_value = json_response['ID']
print(type(id_value))
print(id_value)
url = 'http://216.10.245.166/Library/DeleteBook.php'

delete_payload = {"ID": id_value}
delete_response = requests.post(url, json = delete_payload, headers = {'Content-Type': 'application/json'} )

print(delete_response.text)
print(delete_response.headers)


import json
import configparser

# import requests
#
# url = 'http://216.10.245.166/Library/Addbook.php'
# headers = {"Content-Type": "application/json"}
# addBook_response = requests.post(url, json = payload.add_book_data, headers=headers, )
# print(addBook_response.json())
# response_json = addBook_response.json()
# print(type(response_json))
#
# bookId = response_json['ID']
# print(bookId)
# # Delete Book -
# response_deleteBook = requests.post('http://216.10.245.166/Library/DeleteBook.php', json={
#
#     "ID": bookId
# }, headers={"Content-Type": "application/json"},
#                                     )
#
# # assert response_deleteBook.status_code == 200
# res_json = response_deleteBook.json()
# print(response_deleteBook.status_code)
# print(res_json["msg"])
# # assert res_json["msg"] == "book is successfully deleted"
#
# # #Authentication
# # url = "https://api.github.com/user"
# # github_response = requests.get(url,verify=False,auth=('rahulshettcademy',getPassword()))
# #
# # print(github_response.status_code)


