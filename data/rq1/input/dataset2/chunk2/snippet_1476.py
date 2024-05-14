#Source: https://stackoverflow.com/questions/63325028/why-does-not-raise-typeerror-not-supported-when-all-methods-return-notimple
# Foo __eq__ and Bar __eq__ called
assert not Foo() == Bar()

# Foo __eq__ called twice
f=Foo()
assert f==f