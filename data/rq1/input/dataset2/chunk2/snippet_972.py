#Source: https://stackoverflow.com/questions/70428685/why-do-i-get-a-attributeerror-in-this-code
def total_filesize(images: List[ImageMetadata]):
    total = 0
    try:
        for i in images:
            total = total + i.filesize
    except BaseException as ex:
        logger.error("Caught exception trying to compute total filesize for images", exc_info=True)
    return total