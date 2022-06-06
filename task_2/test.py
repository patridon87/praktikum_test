import inspect
import sys
from io import StringIO


class Capturing(list):
    def __enter__(self):
        self._stdout = sys.stdout
        sys.stdout = self._stringio = StringIO()
        return self

    def __exit__(self, *args):
        self.extend(self._stringio.getvalue().splitlines())
        del self._stringio
        sys.stdout = self._stdout


with Capturing() as output:
    import author


class TestTask2:
    def test_del_print_contact(self):
        assert not hasattr(author, 'print_contact'), \
            'Вы не удалили функцию "print_contact"'

    def test_show_contact_call(self):
        code = inspect.getsource(author)
        assert 'mike.show_contact()' in code, \
            'Вызов метода "show_contact" для экземлпяра ' \
            'класса "mike" не найден'
        assert 'vlad.show_contact()' in code, \
            'Вызов метода "show_contact" для экземлпяра ' \
            'класса "vlad" не найден'

    def test_output(self):
        expected_output = ['Создаём новый контакт Михаил Булгаков',
                           'Создаём новый контакт Владимир Маяковский',
                           'Михаил Булгаков — адрес: Россия, Москва, '
                           'Большая Пироговская, дом 35б, кв. 6, '
                           'телефон: 2-03-27, день рождения: 15.05.1891',
                           'Владимир Маяковский — адрес: Россия, Москва, '
                           'Лубянский проезд, д. 3, кв. 12, телефон: 73-88, '
                           'день рождения: 19.07.1893']
        assert output == expected_output, f'Вывод не соответствует ' \
                                          f'ожидаемому, Ваш вывод: ' \
                                          f'{" ".join(output)}, ' \
                                          f'Ожидаемый вывод: ' \
                                          f'{" ".join(expected_output)}'
