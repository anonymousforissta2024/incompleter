#Source: https://stackoverflow.com/questions/63472025/typeerror-init-got-an-unexpected-keyword-argument-dir
from threading import Timer

message_archive_dir = "achivedir"
message_archive_format = "zip"
archive_timer = Timer(86400, messageachiver.archive, dir = message_archive_dir, fmt = message_archive_format)
archive_timer.start()


class messageachiver(object):
    def __init__(self, **kwargs):
            self.message_archive_dir = dir
            self.message_archive_format = fmt

    def archive(self):
            print("message_archive_dir is " + self.message_archive_dir)
            print("message_archive_format is " + self.message_archive_format)
            print("Archiving trade messages")