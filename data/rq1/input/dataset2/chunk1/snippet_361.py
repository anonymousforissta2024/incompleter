#Source: https://stackoverflow.com/questions/38918748/why-does-mocking-open-and-returning-a-filenotfounderror-raise-attributeerror
import unittest
import unittest.mock as mock

import so_config
import so_main


class TestReadSaveLocation(unittest.TestCase):
    def setUp(self):
        self.savelocation_path = so_config.SAVELOCATION_PATH
        self.root = so_config.ROOT
        so_config.ROOT = 'program root'
        p = mock.patch('so_main.open')
        self.mock_open = p.start()
        self.addCleanup(p.stop)

    def tearDown(self):
        so_config.SAVELOCATION_PATH = self.savelocation_path
        so_config.ROOT = self.root

    def test_read_path_from_disk_file_into_config_py(self):
        self.mock_open().__enter__().readline.return_value = 'data files location'
        so_main.load_savelocation()
        self.assertEqual('data files location', so_config.SAVELOCATION_PATH)

    def test_missing_file_defaults_savelocation_to_program_root(self):
        self.mock_open.return_value = FileNotFoundError
        so_main.load_savelocation()
        self.assertEqual('program root', so_config.SAVELOCATION_PATH)