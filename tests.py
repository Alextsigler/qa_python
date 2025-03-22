from main import BooksCollector
import pytest

# класс TestBooksCollector объединяет набор тестов, которыми мы покрываем наше приложение BooksCollector
# обязательно указывать префикс Test
class TestBooksCollector:

    # пример теста:
    # обязательно указывать префикс test_
    # дальше идет название метода, который тестируем add_new_book_
    # затем, что тестируем add_two_books - добавление двух книг

    @pytest.mark.parametrize('name', ['Комедийная книга', 'Книга ужасов'])
    def test_add_new_book_one_book(self, create_obj_class, name):
        create_obj_class.add_new_book(name)
        assert name in create_obj_class.books_genre

    def test_add_new_book_add_two_books(self, create_obj_class):
        # создаем экземпляр класса BooksCollector с помощью фикстуры create_obj_class

        # добавляем две книги
        create_obj_class.add_new_book('Гордость и предубеждение и зомби')
        create_obj_class.add_new_book('Что делать, если ваш кот хочет вас убить')

        # проверяем, что добавилось именно две
        # словарь books_genre, который нам возвращает метод get_books_genre, имеет длину 2
        assert len(create_obj_class.get_books_genre()) == 2

    # напиши свои тесты ниже
    # чтобы тесты были независимыми в каждом из них создавай отдельный экземпляр класса BooksCollector()

    def test_add_new_book_len_more41_symbol(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        new_book_45_symbol = 'ооооооооооооооооооооочень длинное название книги'

        # добавляем новую книгу
        create_obj_class.add_new_book(new_book_45_symbol)

        # проверяем, что книга не добавилась в словарь book_genre
        assert new_book_45_symbol not in create_obj_class.get_books_genre()

    def test_set_book_genre_add_genre(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        new_book = 'Комедийная книга'
        genre = 'Комедии'

        # добавляем новую книгу
        create_obj_class.add_new_book(new_book)

        # добавляем книге жанр
        create_obj_class.set_book_genre(new_book, genre)

        # проверяем, что для книги установился жанр "Комедии"
        assert new_book, genre in create_obj_class.get_books_genre().items()

    def test_get_book_genre_name_book(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        new_book = 'Книга'
        expected_genre = 'Комедии'

        # добавляем новую книгу
        create_obj_class.add_new_book(new_book)

        # добавляем книге жанр
        create_obj_class.set_book_genre(new_book, expected_genre)

        # проверяем, что жанр совпадает с ожидаемым
        assert create_obj_class.get_book_genre(new_book) == expected_genre

    def test_get_books_with_specific_in_genre_comedy(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        genre_comedy = 'Комедии'
        book_comedy = 'Комедийная книга'

        genre_horror = 'Ужасы'
        book_horror = 'Книга ужасов'

        # добавляем 2 новые книги
        create_obj_class.add_new_book(book_comedy)
        create_obj_class.add_new_book(book_horror)

        # назначаем новым книгам жанр
        create_obj_class.set_book_genre(book_comedy, genre_comedy)
        create_obj_class.set_book_genre(book_horror, genre_horror)

        # проверяем, что вернулась Комедийная книга по жанру Комедии
        assert book_comedy in create_obj_class.get_books_with_specific_genre(genre_comedy)

    def test_test_get_books_with_specific_not_genre_horror(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        genre_comedy = 'Комедии'
        book_comedy = 'Комедийная книга'

        genre_horror = 'Ужасы'
        book_horror = 'Книга ужасов'

        # добавляем 2 новые книги
        create_obj_class.add_new_book(book_comedy)
        create_obj_class.add_new_book(book_horror)

        # назначаем новым книгам жанр
        create_obj_class.set_book_genre(book_comedy, genre_comedy)
        create_obj_class.set_book_genre(book_horror, genre_horror)

        # проверяем, что Книга ужасов не вернулась по жарну Комедии
        assert book_horror not in create_obj_class.get_books_with_specific_genre(genre_comedy)

    def test_get_books_genre_return_books(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        genre_comedy = 'Комедии'
        book_comedy = 'Комедийная книга'

        # добавляем новую книгу
        create_obj_class.add_new_book(book_comedy)

        # добавляем книге жанр
        create_obj_class.set_book_genre(book_comedy, genre_comedy)

        # проверяем, что книга вернулась
        assert book_comedy in create_obj_class.get_books_genre()

    def test_get_books_for_children_not_return_books_horror(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        genre_comedy = 'Комедии'
        book_comedy = 'Комедийная книга'

        genre_horror = 'Ужасы'
        book_horror = 'Книга ужасов'

        # добавляем 2 новые книги
        create_obj_class.add_new_book(book_comedy)
        create_obj_class.add_new_book(book_horror)

        # назначаем новым книгам жанр
        create_obj_class.set_book_genre(book_comedy, genre_comedy)
        create_obj_class.set_book_genre(book_horror, genre_horror)

        # проверяем, что книга несоответствующая рейтингу не вернулась
        assert book_horror not in create_obj_class.get_books_for_children()

    def test_add_book_in_favorites_one_book(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        book_comedy = 'Комедийная книга'

        # добавляем новую книгу
        create_obj_class.add_new_book(book_comedy)

        # добавляем книгу в избранное
        create_obj_class.add_book_in_favorites(book_comedy)

        # проверяем, что книга добавилась в избранное
        assert book_comedy in create_obj_class.favorites

    def test_add_book_in_favorites_has_been_added(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        book_comedy = 'Комедийная книга'

        # добавляем новую книгу
        create_obj_class.add_new_book(book_comedy)

        # добавляем книгу в избранное
        create_obj_class.add_book_in_favorites(book_comedy)

        # повторно добавляем туже книгу в избраное
        create_obj_class.add_book_in_favorites(book_comedy)

        # проверяем, что уже добавленная книга в избранное не добавилась повторно
        assert len(create_obj_class.favorites) == 1

    def test_delete_book_from_favorites_one_book_del_zero_book(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        book_comedy = 'Комедийная книга'

        # добавляем новую книгу
        create_obj_class.add_new_book(book_comedy)

        # добавляем книгу в избранное
        create_obj_class.add_book_in_favorites(book_comedy)

        # удаляем книгу из избранного
        create_obj_class.delete_book_from_favorites(book_comedy)

        # проверяем, что книга удалилась из избранного
        assert len(create_obj_class.favorites) == 0

    def test_get_list_of_favorites_books_all_books(self, create_obj_class):
        # создаем экземпляр (объект) класса BooksCollector с помощью фикстуры create_obj_class

        book_comedy = 'Комедийная книга'
        book_horror = 'Книга ужасов'

        # добавляем новые книги
        create_obj_class.add_new_book(book_comedy)
        create_obj_class.add_new_book(book_horror)

        # добавляем новые книги в избранное
        create_obj_class.add_book_in_favorites(book_comedy)
        create_obj_class.add_book_in_favorites(book_horror)

        # Создаем список для цикла
        book_lst = [book_comedy, book_horror]

        # Проверяем, что обе книги находятся в избранном
        for i in book_lst:
            assert i in create_obj_class.favorites
