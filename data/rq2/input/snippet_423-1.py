import textwrap
sample_text = '\nPython is a widely used high-level, general-purpose, interpreted, dynamic\nprogramming language. Its design philosophy emphasizes code readability,\nand its syntax allows programmers to express concepts in fewer lines of\ncode than possible in languages such as C++ or Java.\n    '
print()
print(textwrap.fill(text1, initial_indent='', subsequent_indent=' ' * 4, width=80))
print()