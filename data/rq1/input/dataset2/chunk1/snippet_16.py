#Source: https://stackoverflow.com/questions/42694112/when-using-pathlib-getting-error-typeerror-invalid-file-posixpathexample-t
from pathlib import Path

filename = Path(__file__).parent / "example.txt"
contents = open(filename, "r").read()