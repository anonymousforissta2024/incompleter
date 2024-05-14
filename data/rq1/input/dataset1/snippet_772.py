# LExecutor: DO NOT INSTRUMENT

# Extracted from https://stackoverflow.com/questions/2461702/why-is-ioc-di-not-common-in-python
# settings.py
from lexecutor.Runtime import _n_
from lexecutor.Runtime import _a_
from lexecutor.Runtime import _c_
from lexecutor.Runtime import _l_
CACHES = {
    'default': {
        'BACKEND': 'django_redis.cache.RedisCache',
        'LOCATION': _n_(1541333, "REDIS_URL", lambda: REDIS_URL) + '/1',
    },
    'local': {
        'BACKEND': 'django.core.cache.backends.locmem.LocMemCache',
        'LOCATION': 'snowflake',
    }
}
_l_(1541334)

class FooView(_n_(1541335, "APIView", lambda: APIView)):
    _l_(1541348)

    # The "injected" dependencies:
    permission_classes = (IsAuthenticated, )
    _l_(1541336)
    throttle_classes = (ScopedRateThrottle, )
    _l_(1541337)
    parser_classes = (_a_(1541338, parsers, "FormParser"), _a_(1541339, parsers, "JSONParser"), _a_(1541340, parsers, "MultiPartParser"))
    _l_(1541341)
    renderer_classes = (_a_(1541342, renderers, "JSONRenderer"),)
    _l_(1541343)

    def get(self, request, *args, **kwargs):
        _l_(1541345)

        pass
        _l_(1541344)

    def post(self, request, *args, **kwargs):
        _l_(1541347)

        pass
        _l_(1541346)

