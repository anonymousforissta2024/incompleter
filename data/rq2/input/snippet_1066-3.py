import textwrap
sample_text = '\n    Python is a widely used high-level, general-purpose, interpreted,\n    dynamic programming language. Its design philosophy emphasizes\n    code readability, and its syntax allows programmers to express\n    concepts in fewer lines of code than possible in languages such\n    as C++ or Java.\n    '
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)
print()
print(final_result)
print()