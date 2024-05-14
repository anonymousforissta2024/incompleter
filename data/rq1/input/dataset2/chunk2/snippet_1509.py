#Source: https://stackoverflow.com/questions/76690265/typeerror-a-bytes-like-object-is-required-not-str-when-trying-to-write-to-a
import os
import bz2
import csv
import traceback


tfile = '/tmp/test.csv.bz'
row = ['bc22jtr', 118324, None, 'contran', None, 11.5, 9.23, ]


def perr(err, bmode, fmode=None):
    """Func for printing exception info in a less noisy manner."""
    print(
        f"EXCEPTION: wt.writerow(row) → {type(err).__name__}:"
        f" {err}; bmode='{bmode}', fmode='{fmode}'"
    )
    print((''.join(traceback.format_exception(err)[-2:-1])).strip())
    return True


for fmode in ["w", "wt", "wb"]:
    for bmode in ["w", "wb"]:
        had_err = False
        if os.path.exists(tfile):
            os.remove(tfile)
        fh = open(tfile, fmode)
        try:
            bh = bz2.BZ2File(fh, mode=bmode, compresslevel=9)
        except ValueError as err:
            had_err = perr(err, bmode, fmode)
        wt = csv.writer(fh)
        try:
            wt.writerow(row)
        except TypeError as err:
            had_err = perr(err, bmode, fmode)
        try:
            bh.close()
        except TypeError as err:
            had_err = perr(err, bmode, fmode)
        if not had_err:
            prnt(f"WAS OK: bmode={bmode}, fmode={fmode}")
for bmode in ["w", "wb", "wt"]:
    if os.path.exists(tfile):
        os.remove(tfile)
    bh = bz2.open(fh, mode=bmode, compresslevel=9)
    wt = csv.writer(fh)
    had_err = False
    try:
        wt.writerow(row)
    except TypeError as err:
        had_err = perr(err, bmode)
    try:
        bh.close()
    except TypeError as err:
        had_err = perr(err, bmode)
    if not had_err:
        prnt(f"WAS OK: bmode={bmode}")
if os.path.exists(tfile):
    os.remove(tfile)