import pytest

from ofdskit.lib.schema import OFDSSchema


@pytest.mark.parametrize(
    "data,path,expected",
    [
        # Get the network id?
        (
            {"networks": [{"id": "a096d627-72e1-4f9b-b129-951b1737bff4"}]},
            ["networks", 0],
            {"network_id": "a096d627-72e1-4f9b-b129-951b1737bff4"},
        ),
        # Get the network and node id?
        (
            {
                "networks": [
                    {
                        "id": "a096d627-72e1-4f9b-b129-951b1737bff4",
                        "nodes": [{"id": "1"}],
                    }
                ]
            },
            ["networks", 0, "nodes", 0],
            {"network_id": "a096d627-72e1-4f9b-b129-951b1737bff4", "node_id": "1"},
        ),
        # Test odd paths that should get nothing
        (
            {
                "networks": [
                    {
                        "id": "a096d627-72e1-4f9b-b129-951b1737bff4",
                        "nodes": [{"id": "1"}],
                    }
                ]
            },
            ["networks"],
            {},
        ),
        # Test odd paths that should get network only
        (
            {
                "networks": [
                    {
                        "id": "a096d627-72e1-4f9b-b129-951b1737bff4",
                        "nodes": [{"id": "1"}],
                    }
                ]
            },
            ["networks", 0, "nodes"],
            {"network_id": "a096d627-72e1-4f9b-b129-951b1737bff4"},
        ),
    ],
)
def test_extract_data_ids_from_data_and_path_1(data, path, expected):
    schema = OFDSSchema()
    output = schema.extract_data_ids_from_data_and_path(data, path)
    assert expected == output
