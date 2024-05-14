#Source: https://stackoverflow.com/questions/46757264/testing-python-asyncio-coroutine-with-pytest-asyncio-plugin-raises-typeerror
class TestController(object):

    @pytest.mark.asyncio
    async def test_get_item(self):

        controller = Controller()
        item = await controller.get_item('item-1')
        assert item.get('item_id') == 'item-1'