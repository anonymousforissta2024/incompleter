#Source: https://stackoverflow.com/questions/55722527/typeerror-cannot-use-a-bytes-pattern-on-a-string-like-object
import re
_WORD_SPLIT = re.compile(b"([.,!?\"':;)(])")

def basic_tokenizer(sentence):
    words = []
    for space_separated_fragment in sentence.strip().split():
        words.extend(_WORD_SPLIT.split(space_separated_fragment))
    return [w for w in words if w]

basic_tokenizer("I live, in Mumbai.")