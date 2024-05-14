#Source: https://stackoverflow.com/questions/59792902/mock-patch-results-in-error-typeerror-object-takes-no-parameters-in-python
class TestSomething(SomeConfigsToBeMixedIn):
    @mock.patch('path.to.BetterParser.parse')
    @mock.patch('path.to.SomeValidator.__new__')
    @mock.patch('path.to.SomeValidator.validate')

    def test_validator_is_called(self, mock_validator_new, mock_parse):
        mock_validator_new.return_value = MockUploadValidator.__new__(MockUploadValidator)
        mock_parse.return_value = mock_csv_details
        mock_validator_new.return_value = MockUploadValidator()

        string_io = build_some_string_io_woohoo()  # this returns a StringIO
        some_file = get_temp_from_stream(string_io)

        upload_manager = CSVUploadManager(a_model_instance, some_file)
        upload_manager.is_valid() # this is where it fails and produces that error

        self.assertTrue(mock_parse.called)
        self.assertTrue(mock_validator_new.called)
        validator_new_call_args = (SomeValidator, self.cash_activity, mock_csv_details)
        self.assertEqual(mock_validator_new._mock_call_args_list[0][0], validator_new_call_args)