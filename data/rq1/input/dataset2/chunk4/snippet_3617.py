#Source: https://stackoverflow.com/questions/66258583/mypy-cannot-detect-nameerror-undefined-variable-unresolved-reference-within-a-fu
def configure():
    undefined_obj.length = 10  # expect NameError: name 'undefined_car' is not defined

configure()