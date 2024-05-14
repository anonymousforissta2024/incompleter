#Source: https://stackoverflow.com/questions/53383631/nameerror-for-variable-that-i-wont-have-value-for-until-runtime
all_fields_dict = {
    'users':
       {
        'first_name': {
            'db_field' : 'FirstName',
            'datatype': 'varchar(50)',
            'test_value': {utils.calc_field_value(['zfill', 'FirstName'])}, # another attempt that didn't work
            'num_bool': False
        },
        'username': {
            'db_field' : 'username',
            'datatype': 'varchar(50)',
            'test_value': f"user{utils.get_random_str(5)}", # this works, but it's a diff kind of calculation
            'num_bool': False,
        },
        'description': {
            'db_field' : 'description',
            'datatype': 'text',
            'test_value': f"{utils.get_desc_info(row_num)}", # one of my attempts - fails
            'num_bool': False,
        },
   }
}