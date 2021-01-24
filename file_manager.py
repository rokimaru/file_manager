from json import loads, dumps
from csv import DictReader

with open("./files/users.json", "r") as f:
    users = loads(f.read())

with open("./files/books.csv", "r") as f:
    reader = DictReader(f)

    lib = []

    for user in users:
        lib_user = {'name': user["name"],
                    'gender': user["gender"],
                    'address': user["address"],
                    }
        book = next(reader)
        lib_book = {"books": [{"title": book["Title"],
                               "author": book["Author"],
                               "height": book["Height"],
                               }]
                    }

        lib_user.update(lib_book)
        lib.append(lib_user)
    print(lib)

with open("./files/result.json", "w") as f:
    f.write(dumps(lib, indent=4))
