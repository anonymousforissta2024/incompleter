#Source: https://stackoverflow.com/questions/68429375/attributeerror-nonetype-object-has-no-attribute-test-using-context-manage
with Tess(foo='bar') as t:
    t.test(foo_bar='baz')