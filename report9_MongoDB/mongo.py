import pymongo

# соединение с Mongo DB по адресу и порту
client = pymongo.MongoClient("mongodb://localhost:27017/")

# создание своей базы данных(контейнер для хранения данных)
db = client["test"]

# создание коллекции(по-другому таблицы)
collection = db["testCollection"]

# добавление данных в коллекцию
data = [
    {'name': 'Karina', 'age': 18},
    {'name': 'Rumiya', 'age': 19},
    {'name': 'Radmir', 'age': 19}
]
collection.insert_many(data)

# Обновление данных в коллекции. $set - это оператор обновления
collection.update_one({'name': 'Karina'}, {'$set': {'age': 19}})

# удаление одного документа из коллекции
collection.delete_one({'name': 'Radmir'})

