#Source: https://stackoverflow.com/questions/77210441/pydantic-typeerror-validate-takes-2-positional-arguments-but-3-were-given
class JsonFeedOptions(BaseModel):
    address: Optional[AddressType] = None
    signer: Optional[Union[AccountAPI, str]] = None
    Type: Optional[FeedType] = None