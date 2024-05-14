#Source: https://stackoverflow.com/questions/41384654/python3-pymongo-typeerror-nonetype-object-is-not-subscriptable-within-cla
from src.common.database import Database

class Admin(object):
    local_settings = Database.find_sort(AdminConstants.COLLECTION, "admin.created_date", -1, 1)