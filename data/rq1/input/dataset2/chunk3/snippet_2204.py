#Source: https://stackoverflow.com/questions/66994103/python-checking-for-empty-list-on-a-path-subclass-is-returning-attributeerror
#!/usr/bin/env python
import os
import pathlib
from pathlib import Path
from typing import Union

class WalkPath(type(pathlib.Path())):
    def __new__(cls, *args, **kwargs):
        return super(WalkPath, cls).__new__(cls, *args, **kwargs)
    
    def __init__(self, *args, dirs: []=[], files: []=[]):
        """Initialize WalkPath object.

        Args:
            dirs (list):        Dirs provided by os.walk(), defauls to []
                                         
            files (list):       Files provided by os.walk(), defaults to []
        """
        
        super().__init__()
        self.dirs: [WalkPath] = [WalkPath(d) for d in dirs]
        self.files: [WalkPath] = [WalkPath(f) for f in files]
    
    @property
    def is_terminus(self):
        return self.is_file() or not self.dirs
    
    @property
    def dirs_abs(self):
        return [self.joinpath(d) for d in self.dirs]
    
    @property
    def files_abs(self):
        return [self.joinpath(f) for f in self.files]
        
    class Utils:

        @staticmethod
        def find_deep(path: Union[str, Path, 'WalkPath']) -> ['WalkPath']:
            """Deeply search the specified dir and return all files and subdirs.
            If path passed is a file, return a list with that single file.

            Args:
                path (str or Path): Root path to search for files.
                
            Returns:
                A filtered list of files or an empty list.
            """

            _path = WalkPath(path) # Coerce to WalkPath
            # print(_path)
            
            if _path.is_file():
                return [_path]

            for root, dirs, files in os.walk(path):
                wp = WalkPath(root, dirs=dirs, files=files)
                for d in wp.dirs_abs:
                    yield d
                    WalkPath.Utils.find_deep(d)

                for f in wp.files_abs:
                    yield WalkPath(f)

paths = WalkPath.Utils.find_deep(Path('/tests/files').resolve())
paths = sorted(paths, key=lambda p: str(p).lower())

for p in paths:
    print(p.parent, p.dirs)