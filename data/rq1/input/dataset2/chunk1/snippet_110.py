#Source: https://stackoverflow.com/questions/35782600/typeerror-generator-missing-1-required-positional-argument-json
for output in output_list:
    output_call = output.generator(json_text)
    print(output_call)