#Source: https://stackoverflow.com/questions/77210441/pydantic-typeerror-validate-takes-2-positional-arguments-but-3-were-given
opts = {"signer": "abcd"}

options = JsonFeedOptions.model_validate(opts)