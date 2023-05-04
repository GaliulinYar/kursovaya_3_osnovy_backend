from utils import list_sort_date


def test_list_sort_date():
    assert list_sort_date.list_sort_date([1, 2, 3, 4, 5, 6, 7]) = [3, 4, 5, 6, 7]
