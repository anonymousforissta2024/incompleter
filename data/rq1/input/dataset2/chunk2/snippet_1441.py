#Source: https://stackoverflow.com/questions/57537309/typeerror-str-returned-non-string-type-magicmock
# mocks.py
image_mock = mock.MagicMock(spec=File, name='FileMock')
image_mock.name = 'dummy.jpg'

storage_mock = mock.MagicMock(spec=Storage, name='StorageMock')
storage_mock.url = mock.MagicMock(name='url')
storage_mock.url.return_value = '/tmp/dummy.jpg'