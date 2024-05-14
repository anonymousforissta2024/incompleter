#Source: https://stackoverflow.com/questions/53383631/nameerror-for-variable-that-i-wont-have-value-for-until-runtime
def get_desc_info():
    row_num = get_row_num()
    return f"Row Num: {row_num} - Wait Time: {wait_time} - Total Inserts: {num_inserts}"

test_value: f"{utils.get_desc_info()}"