import textwrap
text1 = textwrap.dedent(sample_text).strip()
print()
print(textwrap.fill(text1, initial_indent='', subsequent_indent=' ' * 4, width=80))
print()