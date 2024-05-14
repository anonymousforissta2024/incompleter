#Source: https://stackoverflow.com/questions/70428685/why-do-i-get-a-attributeerror-in-this-code
class ImageMetadata(BaseModel):
    title: Optional[str] = None
    source: Optional[str] = None
    sourcesubtype: Optional[str] = None
    filesize: Optional[int] = None
    url: Optional[str] = None