#Source: https://stackoverflow.com/questions/47740542/typeerror-generator-object-is-not-callable
def lines(file):
    for line in file:
        yield line
    yield '\n'

def blocks(file):
    block = []
    for line in lines(file):
        if line.strip():
            block.append(line)
        elif block:
            yield ''.join(block).strip()
            block = []


with open(r'test_input.txt', 'r') as f:
    lines = lines(f)
    file = blocks(lines)
    for line in file:
        print(line)