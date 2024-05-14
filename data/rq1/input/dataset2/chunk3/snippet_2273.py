#Source: https://stackoverflow.com/questions/16778961/attributeerror-map-object-has-no-attribute-extend-in-matplotlib-setup
class Extension(_Extension):
    """Extension that uses '.c' files in place of '.pyx' files"""

    if not have_pyrex:
        # convert .pyx extensions to .c 
        def __init__(self,*args,**kw):
            _Extension.__init__(self,*args,**kw)
            sources = []
            for s in self.sources:
                if s.endswith('.pyx'):
                    sources.append(s[:-3]+'c')
                else:
                    sources.append(s)
            self.sources = sources