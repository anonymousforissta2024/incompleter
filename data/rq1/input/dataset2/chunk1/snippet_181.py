#Source: https://stackoverflow.com/questions/68554023/typeerror-init-subclass-takes-no-keyword-arguments-related-to-subclass-an
class case1(Pipeline):
    def read_data(self):
        return pd.read_csv("file location") # just hard coding for the file location

   
    @property
    def used_cols(self, selected_cols):
        return selectd_cols