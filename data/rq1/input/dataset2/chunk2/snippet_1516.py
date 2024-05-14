#Source: https://stackoverflow.com/questions/76196828/nameerror-global-name-open-is-not-defined-error-in-init-py-file
class CustomAgent(Agent.Movies):
    def update(self, metadata, media, lang):
        with open("db.tsv", "r") as fp:
            line = fp.readline()
            while line:
                ...