BOOKS_DATABASE = [
    {
        "id": 1,
        "name": "test_name_1",
        "pages": 200,
    },
    {
        "id": 2,
        "name": "test_name_2",
        "pages": 400,
    }
]


# TODO написать класс Book
class Book:
    def __init__(self, id_: int, name: str, pages: int):
        self.id_ = None
        self.name = None
        self.pages = None
        self.init_id(id_)
        self.init_name(name)
        self.init_pages(pages)

    def init_id(self, id_: int):
        if not isinstance(id_, int) or id_ < 0:
            raise TypeError('Номер книги должен быть целым положительным числом')
        self.id_ = id_

    def init_name(self, name: str):
        if not isinstance(name, str):
            raise TypeError('Название книги должно состоять из букв')
        self.name = name

    def init_pages(self, pages: int):
        if not isinstance(pages, int) or pages < 0:
            raise TypeError('Страница книги должна быть целым положительным числом')
        self.pages = pages



    def __str__(self):
        return f'Книга {self.name}'

    def __repr__(self):
        return f'{self.__class__.__name__}(id_={self.id_}, name={self.name}, pages={self.pages})'

if __name__ == '__main__':
    # инициализируем список книг
    list_books = [
        Book(id_=book_dict["id"], name=book_dict["name"], pages=book_dict["pages"]) for book_dict in BOOKS_DATABASE
    ]
    for book in list_books:
        print(book)  # проверяем метод __str__

    print(list_books)  # проверяем метод __repr__
