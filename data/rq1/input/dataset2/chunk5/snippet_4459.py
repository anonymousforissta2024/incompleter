#Source: https://stackoverflow.com/questions/55288202/adding-uuid-type-to-cerberus-leads-to-bad-type-error
@pytest.mark.unit
def test_valid_uuid():
    test_input = "35d6d5a0-6f37-4794-a493-2712eda41c1a"
    actual = UUID(test_input)
    assert str(actual) == "35d6d5a0-6f37-4794-a493-2712eda41c1a"

@pytest.mark.unit
def test_invalid_uuid():
    test_input = "Not a Valid UUID"
    with pytest.raises(ValueError):
        actual = UUID(test_input) 

@pytest.mark.unit
def test_uuid_type_registration():
    test_schema = {"test_name": {"type": "UUID"}}
    validator = Validator(test_schema)
    test_record = {"test_name": "35d6d5a0-6f37-4794-a493-2712eda41c1a"}
    result = validator.validate(test_record)
    print(validator._errors)
    assert result == True