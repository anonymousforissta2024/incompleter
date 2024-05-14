#Source: https://stackoverflow.com/questions/60616722/typeerror-when-chunking-subtasks-in-grouped-tasks
#!/usr/bin/env python3

from celery import Celery, group
from io import BytesIO
import time
import xlsxwriter
import argparse
import sys

# Celery related :

app = Celery('tasks', broker='amqp://admin:mypass@rabbit', backend='rpc://')

def apply_power(entry, power):
    time.sleep(0.01)
    return entry ** power

def make_data_for_entry(entries, power):
    return [(entry, apply_power(entry, power)) for entry in entries]

@app.task
def decorated_make_data_for_entry(*args):
    return make_data_for_entry(*args)

@app.task
def make_worksheet_data(entries, power, header, chunks):
    if chunks is not None:
        result = decorated_make_data_for_entry.chunks(zip(entries), chunks)(power)
        result = make_data_for_entry.chunks(zip(entries), chunks)(power)
    else:
        result = make_data_for_entry(entries, power)
    return [header] + result

@app.task
def decorated_make_worksheet_data(*args):
    return make_worksheet_data(*args)

def make_worksheet_from_data(workbook, worksheet_data, name):
    worksheet = workbook.add_worksheet(name)
    for i, row in enumerate(worksheet_data):
        for j, cell in enumerate(row):
            worksheet.write(i, j, cell)

def generate_output(parsed_args, output):
    workbook = xlsxwriter.Workbook(output)
    entries = range(parsed_args.entries)
    if parsed_args.multi is not None:
        g = group([
            decorated_make_worksheet_data.s(list(entries), 2, ["value", "square"], parsed_args.chunks),
            decorated_make_worksheet_data.s(list(entries), 3, ["value", "cube"], parsed_args.chunks),
        ])  # also tried without the []
        result = g()
        result_get = result.get()
        worksheet_square_data, worksheet_cube_data = result_get
    else:
        worksheet_square_data = make_worksheet_data(list(entries), 2, ["value", "square"], parsed_args.chunks)
        worksheet_cube_data = make_worksheet_data(list(entries), 3, ["value", "cube"], parsed_args.chunks)
    make_worksheet_from_data(workbook, worksheet_square_data, "square")
    make_worksheet_from_data(workbook, worksheet_cube_data, "cube")
    workbook.close()

@app.task
def generate_file_from_output(parsed_args):
    output = BytesIO()
    generate_output(parsed_args, output)
    with open("/dump/file.xlsx", "wb") as f:
        output.seek(0)
        f.write(output.read())

def main():
    generate_file_from_output()

if __name__ == "__main__":
    main()