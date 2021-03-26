from main import documents, directories, print_name, print_shelf_number, add_data
class Test:
    def setup(self):
        print('method setup')

    def teardown(self):
        print("method teardown")

    def test_print_name(self):
        assert print_name('2207 876234') == 'Василий Гупкин'
        assert print_name('11-2') == 'Геннадий Покемонов'
        assert print_name('10006') == 'Аристарх Павлов'

    def test_print_shelf_number(self):
        assert print_shelf_number('2207 876234') == ('Документ на полке','1')
        assert print_shelf_number('11-2') == ('Документ на полке','1')
        assert print_shelf_number('10006') == ('Документ на полке','2')

    def test_add_data(self):
        assert add_data('vasya','passport','000',3) == ([
    {"type": "passport", "number": "2207 876234", "name": "Василий Гупкин"},
    {"type": "invoice", "number": "11-2", "name": "Геннадий Покемонов"},
    {"type": "insurance", "number": "10006", "name": "Аристарх Павлов"},
    {"type": "passport", "number": "000", "name": "vasya"}
], {
    '1': ['2207 876234', '11-2', '5455 028765'],
    '2': ['10006'],
    '3': ['000']
})