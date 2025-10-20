import sys
import json

books = [
    {
        "title":"java基礎",
        "author":"佐藤花子",
        "year":2023,
        "isbn":"978-4-987654-32-1",
        "price":2800
    },
    {
        "title":"web開発",
        "author":"山田次郎",
        "year":2023,
        "isbn":"978-4-111111-11-1",
        "price":3200
    }
]

new_data_json = sys.argv[1]
new_data = json.loads(new_data_json)
books.append(new_data)

print("本データベース")
print(books)