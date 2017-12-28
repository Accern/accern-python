import json

def test_options_valid():
    FIELD_OPTIONS = json.load(open("./accern/data/options.json"))
    assert isinstance(FIELD_OPTIONS, object)
