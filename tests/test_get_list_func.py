from utils.get_list_func import get_list_operation


def test_get_list_func():
    write_collection = [{'id': 587085106, 'state': 'EXECUTED', 'date': '2018-03-23T10:45:06.972075', 'operationAmount': {'amount': '48223.05', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 41421565395219882431'}, {'id': 142264268, 'state': 'EXECUTED', 'date': '2019-04-04T23:20:05.206878', 'operationAmount': {'amount': '79114.93', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 19708645243227258542', 'to': 'Счет 75651667383060284188'}, {'id': 873106923, 'state': 'EXECUTED', 'date': '2019-03-23T01:09:46.296404', 'operationAmount': {'amount': '43318.34', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод со счета на счет', 'from': 'Счет 44812258784861134719', 'to': 'Счет 74489636417521191160'}, {'id': 214024827, 'state': 'EXECUTED', 'date': '2018-12-20T16:43:26.929246', 'operationAmount': {'amount': '70946.18', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 10848359769870775355', 'to': 'Счет 21969751544412966366'}, {'id': 522357576, 'state': 'EXECUTED', 'date': '2019-07-12T20:41:47.882230', 'operationAmount': {'amount': '51463.70', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Счет 48894435694657014368', 'to': 'Счет 38976430693692818358'}, {'id': 895315941, 'state': 'EXECUTED', 'date': '2018-08-19T04:27:37.904916', 'operationAmount': {'amount': '56883.54', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'Visa Classic 6831982476737658', 'to': 'Visa Platinum 8990922113665229'}, {'id': 596171168, 'state': 'EXECUTED', 'date': '2018-07-11T02:26:18.671407', 'operationAmount': {'amount': '79931.03', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Открытие вклада', 'to': 'Счет 72082042523231456215'}, {'id': 716496732, 'state': 'EXECUTED', 'date': '2018-04-04T17:33:34.701093', 'operationAmount': {'amount': '40701.91', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод организации', 'from': 'Visa Gold 5999414228426353', 'to': 'Счет 72731966109147704472'}, {'id': 863064926, 'state': 'EXECUTED', 'date': '2019-12-08T22:46:21.935582', 'operationAmount': {'amount': '41096.24', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Открытие вклада', 'to': 'Счет 90424923579946435907'}, {'id': 147815167, 'state': 'EXECUTED', 'date': '2018-01-26T15:40:13.413061', 'operationAmount': {'amount': '50870.71', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод с карты на счет', 'from': 'Maestro 4598300720424501', 'to': 'Счет 43597928997568165086'}, {'id': 518707726, 'state': 'EXECUTED', 'date': '2018-11-29T07:18:23.941293', 'operationAmount': {'amount': '3348.98', 'currency': {'name': 'USD', 'code': 'USD'}}, 'description': 'Перевод с карты на карту', 'from': 'MasterCard 3152479541115065', 'to': 'Visa Gold 9447344650495960'}, {'id': 649467725, 'state': 'EXECUTED', 'date': '2018-04-14T19:35:28.978265', 'operationAmount': {'amount': '96995.73', 'currency': {'name': 'руб.', 'code': 'RUB'}}, 'description': 'Перевод организации', 'from': 'Счет 27248529432547658655', 'to': 'Счет 97584898735659638967'}]


    assert get_list_operation('./tests/test_file.json') == write_collection
    assert get_list_operation('./tests/test_file2.json') == []
    assert get_list_operation('./tests/test_file3.json') == []