#Source: https://stackoverflow.com/questions/51902851/repeated-fields-return-attributeerror-type-object-foo-has-no-attribute-nums
import main_pb2
foo = main_pb2.Foo
foo.nums.append(1)