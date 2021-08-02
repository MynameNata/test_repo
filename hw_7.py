import requests
import json

base_url = "http://pulse-rest-testing.herokuapp.com/"
head = {'Content-Type': 'application/json'}

book_dict = json.dumps({
    "title": "Flowers for Algeron",
    "author": "Daniel Keyes"
})
book_dict_new = json.dumps({
    "title": "Second_one_Flowers for Algeron",
    "author": "_Second_one_Daniel Keyes"
})


create_book = requests.post(base_url + '/books', headers = head, data=book_dict)
my_book_dict = create_book.json()
id_book = my_book_dict['id']
get_my_book = requests.get(base_url + '/books/' + str(id_book))
#
in_list = requests.get(base_url + '/books')

create_book_new_one = requests.post(base_url + '/books', headers = head, data=book_dict_new)
in_list_2 = requests.get(base_url + '/books')

role_new = json.dumps({
        "name": "Algeron",
        "type": "mouse",
        "level": 1,
        "book": 3244
    })

create_role = requests.post(base_url + '/roles', headers = head, data=role_new)



print(id_book)
print(my_book_dict)

print(in_list.json())
print(create_book.request.headers)
print(create_book.headers)
print(create_book.request.body)
print(get_my_book.url)
print(create_book_new_one.status_code)
print(create_book_new_one.request.body)
print(in_list_2.json())
print(in_list.json())
print(create_role.json())