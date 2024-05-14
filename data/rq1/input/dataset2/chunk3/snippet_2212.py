#Source: https://stackoverflow.com/questions/16778961/attributeerror-map-object-has-no-attribute-extend-in-matplotlib-setup
class Extension(_Extension):
    """Extension that uses '.c' files in place of '.pyx' files"""

    def __init__(self, *args, **kw):
        _Extension.__init__(self, *args, **kw)
        if not have_pyrex():
            self._convert_pyx_sources_to_c()

    def _convert_pyx_sources_to_c(self):
        "convert .pyx extensions to .c"
        def pyx_to_c(source):
            if source.endswith('.pyx'):
                source = source[:-4] + '.c'
            return source
        self.sources = map(pyx_to_c, self.sources)