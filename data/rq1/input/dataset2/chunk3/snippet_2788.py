#Source: https://stackoverflow.com/questions/58012400/compiling-json-schema-using-fastjsonschema-gives-typeerror-string-indices-must
import fastjsonschema

schema_file = open(schema.json)
schema_str = schema_file.read()
validatation = fastjsonschema.compile(schema_str)