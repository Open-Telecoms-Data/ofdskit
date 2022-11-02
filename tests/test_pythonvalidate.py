import json
import os

import pytest

from ofdskit.lib.pythonvalidate import PythonValidate
from ofdskit.lib.schema import OFDSSchema

PYTHONVALIDATE_FILES = [
    ("basic_1"),
    ("end_node_not_found_1"),
    ("node_international_connections_country_not_set_1"),
    ("node_location_coordinates_incorrect_1"),
    ("node_location_type_incorrect_1"),
    ("node_not_used_in_any_spans_1"),
    ("organisation_id_not_found_1"),
    ("organisation_name_not_match_1"),
    ("organisation_reference_name_set_but_not_in_original_1"),
    ("phase_id_not_found_1"),
    ("phase_name_not_match_1"),
    ("phase_reference_name_set_but_not_in_original_1"),
    ("span_route_coordinates_incorrect_1"),
    ("span_route_type_incorrect_1"),
    ("start_node_not_found_1"),
    ("start_node_not_found_but_has_external_nodes_1"),
]


@pytest.mark.parametrize(
    "filename",
    PYTHONVALIDATE_FILES,
)
def test_basic_1(filename):
    input_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "pythonvalidate",
        filename + ".input.json",
    )
    expected_filename = os.path.join(
        os.path.dirname(os.path.realpath(__file__)),
        "fixtures",
        "pythonvalidate",
        filename + ".expected.json",
    )

    with open(input_filename) as fp:
        input_data = json.load(fp)
    with open(expected_filename) as fp:
        expected_data = json.load(fp)

    print(expected_data)

    schema = OFDSSchema()
    validate = PythonValidate(schema)
    output = validate.validate(input_data)

    # Library is not meant to return these in any special order, so sort by type to get something we can check.
    output = sorted(output, key=lambda d: d["type"] + d.get("field", ""))

    assert expected_data == output
