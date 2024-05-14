#Source: https://stackoverflow.com/questions/46100312/streaming-data-from-amazon-s3-using-smart-open-causing-typeerror
import smart_open

def stream_data():
    my_bucket = 'monkey-business-dev'
    my_key = 'incoming_monkey_data/banana/banana'
    uri = 's3://{}/{}'.format(my_bucket, my_key)
    total_lines = 0
    total_records = 0
    for line in smart_open.smart_open(uri):
        total_records += 1


if __name__ == '__main__':
    stream_data()