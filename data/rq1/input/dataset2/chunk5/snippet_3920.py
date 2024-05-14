#Source: https://stackoverflow.com/questions/53620627/python-from-import-works-but-import-throws-typeerror
import logging
import k8s.instance
import k8s.projects_v2
from typing import Union

CELL_KEY: str = 'cell'

CELLS_KEY: str = 'cells'

EXTENDS_KEY: str = 'extends'


_logging = logging.getLogger(__name__)


class Cell(k8s.instance.Instance):

    def __init__(self):
        super().__init__()

        self.__projects = k8s.projects_v2.Projects()