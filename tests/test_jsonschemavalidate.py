import json
import os

import pytest

from ofdskit.lib.jsonschemavalidate import JSONSchemaValidator
from ofdskit.lib.schema import OFDSSchema

JSONSCHEMAVALIDATE_FILES = [
    # basic example
    ("basic_1"),
]


@pytest.mark.parametrize(
    "filename",
    JSONSCHEMAVALIDATE_FILES,
)
def test_jsonschemavalidate(filename):
    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "jsonschemavalidate",
        filename + ".input.json",
    )
    expected_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "jsonschemavalidate",
        filename + ".expected.json",
    )

    with open(input_filename) as fp:
        input_data = json.load(fp)
    with open(expected_filename) as fp:
        expected_data = json.load(fp)

    schema = OFDSSchema()
    validator = JSONSchemaValidator(schema)
    results = validator.validate(input_data)
    results_json = [r.json() for r in results]

    assert expected_data == results_json
