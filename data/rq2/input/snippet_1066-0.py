import textwrap
text_without_Indentation = textwrap.dedent(sample_text)
wrapped = textwrap.fill(text_without_Indentation, width=50)
final_result = textwrap.indent(wrapped, '> ')
print()
print(final_result)
print()