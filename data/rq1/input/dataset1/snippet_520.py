# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/16694907/download-large-file-in-python-with-requests
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
try:
    import aiofiles
    _l_(1545956)

except ImportError:
    pass
try:
    import aiohttp
    _l_(1545958)

except ImportError:
    pass
try:
    import asyncio
    _l_(1545960)

except ImportError:
    pass

async def async_http_download(src_url, dest_file, chunk_size=65536):
    _l_(1545986)

    async with _c_(1545964, _a_(1545962, _n_(1545961, "aiofiles", lambda: aiofiles), "open"), _n_(1545963, "dest_file", lambda: dest_file), 'wb') as fd:
        _l_(1545985)

        async with _c_(1545967, _a_(1545966, _n_(1545965, "aiohttp", lambda: aiohttp), "ClientSession")) as session:
            _l_(1545984)

            async with _c_(1545971, _a_(1545969, _n_(1545968, "session", lambda: session), "get"), _n_(1545970, "src_url", lambda: src_url)) as resp:
                _l_(1545983)

                async for chunk in _c_(1545976, _a_(1545974, _a_(1545973, _n_(1545972, "resp", lambda: resp), "content"), "iter_chunked"), _n_(1545975, "chunk_size", lambda: chunk_size)):
                    _l_(1545982)

                    await _c_(1545980, _a_(1545978, _n_(1545977, "fd", lambda: fd), "write"), _n_(1545979, "chunk", lambda: chunk))
                    _l_(1545981)

SRC_URL = "/path/to/url"
_l_(1545987)
DEST_FILE = "/path/to/file/on/local/machine"
_l_(1545988)

_c_(1545995, _a_(1545990, _n_(1545989, "asyncio", lambda: asyncio), "run"), _c_(1545994, _n_(1545991, "async_http_download", lambda: async_http_download), _n_(1545992, "SRC_URL", lambda: SRC_URL), _n_(1545993, "DEST_FILE", lambda: DEST_FILE)))
_l_(1545996)

