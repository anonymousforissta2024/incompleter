#Source: https://stackoverflow.com/questions/58163433/python-concurrent-futures-typeerror-zip-argument-1-must-support-iteration
def documents_processing(skip):
    conn = get_connection()
    db = conn["db_name"]

    print("Process::{} -- db.Transactions.find(no_cursor_timeout=True).skip({}).limit(10000)".format(os.getpid(), skip))
    documents = db.Transactions.find(no_cursor_timeout=True).skip(skip).limit(10000)
    # Do some processing in mongodb


max_workers = 20


def skip_list():
    for i in range(0, 100000, 10000):
        yield [j for j in range(i, i + 10000, 1000)]


def main_f():
    try:
        with concurrent.futures.ProcessPoolExecutor(max_workers=max_workers) as executor:
            executor.map(documents_processing, skip_list)
    except Exception:
        print("exception:", traceback.format_exc())

main_f()