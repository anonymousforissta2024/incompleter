#Source: https://stackoverflow.com/questions/49821328/pyspark-udf-attributeerror-nonetype-object-has-no-attribute-jvm
@staticmethod
@F.udf("array<int>")
def create_users_array(val):
    """ Takes column of ints, returns column of arrays containing ints. """ 
    return [val for _ in range(val)]