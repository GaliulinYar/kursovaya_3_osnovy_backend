from datetime import datetime


class Change:

    def __init__(self, date='', from_operation='', to_operation=''):
        # Дата из последних 5 операций
        self.date = date
        # откуда операци
        self.from_operation = from_operation
        # куда операция
        self.to_operation = to_operation

    def __repr__(self):
        return f'{self.__class__.__name__}' \
               f'Дата = {self.date}' \
               f'Операция от кого = {self.from_operation}' \
               f'Операция кому = {self.to_operation}'

    def change_date(self):
        """Метод изменяет дату на нужную"""
        date_from_str = datetime.strptime(self.date, '%Y-%m-%dT%H:%M:%S.%f')
        return date_from_str.strftime('%d %m %Y')

    def change_from_operation(self):
        """метод скрывает цифры карты или счета ОТ КОГО отправлено"""
        split_list = self.from_operation.split(' ')
        if len(split_list[-1]) == 16:
            split_number = 'XXXX XX' + split_list[-1][6:8] + ' ' + split_list[-1][8:-4] + ' XXXX'

            return ' '.join(split_list[:-1]) + ' ' + str(split_number)
        else:
            split_from = 'X' * (len(split_list[-1]) - 4) + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_from)

    def change_to_operation(self):
        """метод скрывает цифры карты или счета КУДА отправлено"""
        split_list = self.to_operation.split(' ')
        if len(split_list[-1]) == 16:
            split_number = 'XXXX XX' + split_list[-1][6:8] + ' ' + split_list[-1][8:-4] + ' XXXX'
            return ' '.join(split_list[:-1]) + ' ' + str(split_number)
        else:
            split_from = 'X' * (len(split_list[-1]) - 4) + split_list[-1][-4:]
            return ' '.join(split_list[:-1]) + ' ' + str(split_from)
