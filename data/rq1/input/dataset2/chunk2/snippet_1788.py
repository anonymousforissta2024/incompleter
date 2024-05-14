#Source: https://stackoverflow.com/questions/56246570/typeerror-init-missing-1-required-positional-argument-branches-but-argu
class CvGerrit(Gerrit):
    def __init__(self, segment, rev_id, branches):
        Gerrit.__init__(segment, rev_id, branches)