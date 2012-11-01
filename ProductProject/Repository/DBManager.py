class DBManager(object):
    def __init__(self, file_name, file_open_mode):
        self.__enter__(file_name, file_open_mode)

    def __enter__(self, file_name, file_open_mode):
        pass

    def __exit__(self):
        pass

    def get_string(self, index):
        pass

    def set_string(self, index, string):
        pass

    def create_index_file_main(self):
        pass

    def create_index_file_by_field(self, field):
        pass
