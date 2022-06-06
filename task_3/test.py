import sys
import time
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
    start_time = time.time()
    import author
    spend_time = time.time() - start_time


class TestTask3:
    def test_output(self):
        expected_output = ['Время выполнения функции: 1.0 с.', '2',
                           'Время выполнения функции: 0.0 с.', '2',
                           'Время выполнения функции: 1.0 с.', '4',
                           'Время выполнения функции: 0.0 с.', '4',
                           'Время выполнения функции: 0.0 с.', '4']

        assert output == expected_output, f'Вывод не соответствует ' \
                                          f'ожидаемому, Ваш вывод: ' \
                                          f'{" ".join(output)}, ' \
                                          f'Ожидаемый вывод: ' \
                                          f'{" ".join(expected_output)}'

    def test_time(self):
        """Проверка, что студент написал декоратор, а не сделал нужный print"""

        assert spend_time >= 2.0, 'Слишком быстрое выполнение программы,' \
                                  'проверьте, что не удалили код функции' \
                                  '"time_check"'
