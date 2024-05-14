#Source: https://stackoverflow.com/questions/73656349/typeerror-list-indices-must-be-integers-or-slices-not-str-when-i-try-to-iterat
colloquial_numbers = ['veinti[\\s|-|]tres', 'veinti[\\s|-|]dos', 'veinti[\\s|-|]uno', 'veinte', 'tres', 'dos', 'uno']

symbolic_numbers = ['23', '22', '21', '20', '3', '2', '1']

body = ''
for n in coloquial_numbers:
    body += """    input_text = re.sub(r"{}", "{}", input_text)\n""".format(coloquial_numbers[n], symbolic_numbers[n])
    #body += """    input_text = re.sub(r'""" + coloquial_numbers[n] + """', '""" + symbolic_numbers[n] + """', input_text)\n"""

print(repr(body))