# qa_python

            Описаие тестов


- Проверяет возможность добавления книги в словарь books_genre
  test_add_new_book_one_book

  
- Проверяет возможность добавления 2-х книг в словарь books_genre,
исправлен, был указан не правильный метод
  test_add_new_book_add_two_books


- Проверяет валидацию сохранения книги более 41 символа
  test_add_new_book_len_more41_symbol


- Проверяет, что для книги устанавливается жанр
  test_set_book_genre_add_genre

  
- Проверяет, что жанр книги совпадает с ожидаемым
  test_get_book_genre_name_book

  
- Проверяет, что вернулась правильная книга по выбранному жарну
  test_get_books_with_specific_in_genre_comedy

  
- Проверяет, что книга не относящаяся к выбранному жанру не вернулась
  test_test_get_books_with_specific_not_genre_horror

  
- Проверяет, что книга вернулась
  test_get_books_genre_return_books


- Проверяет, что книга несоответствующая рейтингу не вернулась
  test_get_books_for_children_not_return_books_horror

  
- Проверяет, что книга добавлена в избранное
  test_add_book_in_favorites_one_book

  
- Проверяет, что уже добавленная книга в избранное не добавилась повторно
  test_add_book_in_favorites_has_been_added

  
- Проверяет, что книга удалилась из избранного
  test_delete_book_from_favorites_one_book_del_zero_book

  
- Проверяет, что обе книги находятся в избранном
  test_get_list_of_favorites_books_all_books