#Source: https://stackoverflow.com/questions/55012786/typeerror-close-spider-missing-1-required-positional-argument-reason
import sqlite3 as sq3
import sqlite3_functions as sq_f
import logging
from scrapy.exceptions import DropItem

class CointelegraphSpiderPipeline(object):
    """
    Doc string
    """

    def __init__(self, stats):
        """
        Doc string
        """
        self.stats = stats
        self.db_file = 'D:\\DCC\\Projects\\crypto_projects\\master_data.db'
        self.conn = sq3.connect(self.db_file)
        self.table_name = 'cointelegraph'
        self.commit_counter = 0


    @classmethod
    def from_crawler(cls, crawler):
        """
        Doc string
        """
        stats = crawler.stats
        return stats   #cls(crawler.stats)

    def open_spider(self, spider):
        """
        Doc string
        """
        print("I'm starting the pipeline")
        logging.INFO("Starting Pipeline...")

    def process_item(self, item, spider):
        """
        Doc string
        """
        item_checked = True

        try:
            # Sanity Check
            for key, value in item.items():
                print("Inside the loop!!!")
                if value == '':
                    item_checked = False
                    raise DropItem("Item '{0}:{1}' has empty data - Link: {3}".format(key, value, item['link']))
                else:
                    logging.INFO("Item check OK")
                    item_checked = True

            # Insert row and increase counter
            if item_checked:
                self.conn = sq_f.insert_row(self.db_file, table_name=self.table_name, conn=self.conn, **item)
                self.commit_counter += 1
                self.conn.commit()

            # Commit every 500 inserted rows
            if self.commit_counter % 500 == 0:
                self.conn.commit()

            print(item)

        except Exception as e:
            logging.WARNING(e)




    def close_spider(self, spider):
        """
        Doc string
        """
        logging.INFO("Commiting rows...")
        self.conn.commit()
        logging.INFO("Saving spider stats...")
        print(self.stats.get_stats())
        logging.INFO("Closing pipeline..")
        self.conn.close()