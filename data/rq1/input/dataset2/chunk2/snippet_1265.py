#Source: https://stackoverflow.com/questions/42122240/sqlite-typeerror-query-takes-2-positional-arguments-but-4-were-given
from db_manage import inv_enq

def main():
    ord_numb = input('Enter Order Number > ')
    part_numb = input('Enter Part Number > ')
    inv_enq(ord_numb, part_numb)

if __name__ == "__main__":
    main()