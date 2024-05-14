#Source: https://stackoverflow.com/questions/60990112/typeerror-fit-takes-1-positional-argument-but-3-were-given
myclass = MyClass(path1, path2)
skl_pipeline = Pipeline(steps=[('myclass', myclass)])
skl_pipeline.fit(None)