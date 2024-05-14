#Source: https://stackoverflow.com/questions/57535901/pytest-getting-attributeerror-capturefixture-object-has-no-attribute-readou
import pytest

def test_can_output_to_stdout(capsys):
    print("hello")
    capture = capsys.readouterror()
    assert "hello" in capture.out