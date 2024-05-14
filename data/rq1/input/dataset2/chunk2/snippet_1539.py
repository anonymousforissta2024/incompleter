#Source: https://stackoverflow.com/questions/66450526/typeerror-nonetype-object-is-not-callable-when-passing-arguments-to-decorator
def mytimeit_with_args(stuff_to_print):
    def decorator(f):
        def func(*args, **kwargs):
            start = time.time()
            result = f(*args, **kwargs)
            print(stuff_to_print)
            print(f"Function took {time.time() - start} seconds to run.")
            return result
        return func

@mytimeit_with_args("just some stuff")
def harder_loop(n=10, sleep=0.2):
    for i in range(n):
        time.sleep(sleep)