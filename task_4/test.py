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


class TestTask4:
    def test_make_divider_of_call(self):
        code = inspect.getsource(author)
        assert 'div2 = make_divider_of(2)' in code, \
            'Проверьте, что не удалили переменную div2'
        assert 'div5 = make_divider_of(5)' in code, \
            'Проверьте, что не удалили переменную div5'

    def test_output(self):
        expected_output = ['5.0', '4.0', '2.0']
        assert output == expected_output, f'Вывод не соответствует ' \
                                          f'ожидаемому, Ваш вывод: ' \
                                          f'{" ".join(output)}, ' \
                                          f'Ожидаемый вывод: ' \
                                          f'{" ".join(expected_output)}'
