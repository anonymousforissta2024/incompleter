#Source: https://stackoverflow.com/questions/61365330/celery-running-signature-from-database-attributeerror-object-has-no-attribute
object_1 # Signature
object_2 # Signature
object_3 # _chain

ch = object_1 | object_2 | object_3
ch.apply_async()