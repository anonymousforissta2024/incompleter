#Source: https://stackoverflow.com/questions/59756898/within-contextlib-redirect-stdout-the-print-function-causes-an-attributeerro
dummy_file = "dummy_textfile.txt"  # file to which the stdout shall be redirected

with contextlib.redirect_stdout(dummy_file):
    # Direct print()-function call
    print("Informative string which shall go to the textfile instead of the console.")

    # Indirect print()-function calls (internally)
    custom_function_with_internal_print_calls(**kwargs)