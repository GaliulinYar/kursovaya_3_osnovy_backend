
from utils import get_list_func


def test_get_list_func():

    assert get_list_func.get_list_func('/home/yaroslav/kursovaya_3_osnovy_backend/tests/test_file.json') == [{"state": "EXECUTED", "operation": "op1"}, {"state": "EXECUTED", "operation": "op2"}]
    assert get_list_func.get_list_func('/home/yaroslav/kursovaya_3_osnovy_backend/tests/test_file2.json') == []
    assert get_list_func.get_list_func('/home/yaroslav/kursovaya_3_osnovy_backend/tests/test_file2.json') == []

