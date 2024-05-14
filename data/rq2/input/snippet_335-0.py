import platform as pl
for key in os_profile:
    if hasattr(pl, key):
        print(key + ': ' + str(getattr(pl, key)()))