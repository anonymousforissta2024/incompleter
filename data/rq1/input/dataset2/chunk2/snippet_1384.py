#Source: https://stackoverflow.com/questions/56246570/typeerror-init-missing-1-required-positional-argument-branches-but-argu
class Gerrit:
    connections = {
        'consumer': MyGerritClient(host='gerrit.consumer.com', username=getpass.getuser()),
        'b2b': MyGerritClient(host='gerrit.b2b.com', username=getpass.getuser())
    }

    def __init__(self, segment, rev_id, branches):
        print("TRACE: Gerrit::__init__()")
        self.branches = branches
        self.review = None  # Type: GerritChange
        self.gerrit_client = self.connections[segment]
        for review_candidate in self.gerrit_client.query(rev_id):
            if self.branch_is_valid(review_candidate.branch) and review_candidate.status != 'ABANDONED':
                self.review = review_candidate
        self.approved = False
        self.rev_id = rev_id
        self.merged = False