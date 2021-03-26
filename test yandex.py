from yandex import create_folder
class Test:
    def setup(self):
        print('method setup')

    def teardown(self):
        print("method teardown")

    def test_create_folder(self):
        assert create_folder('fff') == '<Response [201]>'