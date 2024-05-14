#Source: https://stackoverflow.com/questions/45000350/getting-attributeerror-during-instantiation-of-subclass
class Keyword(Cipher):
    converted_string = []

    def __init__(self, secret_string, *args, **kwargs):
        if len(self.secret_string) < 1:
            raise ValueError("Secret string cannot be empty")
        super().__init__(secret_string)

    @property
    def convert_to_keyword_string(self):
        for num in self.secret_numbers:
            for k, v in self.orig_dict:
                if num == v:
                    self.converted_string.append(k)
        return self.converted_string