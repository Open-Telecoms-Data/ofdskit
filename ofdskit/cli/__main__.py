import argparse
import json

import ofdskit.lib.geojson
import ofdskit.lib.jsonschemavalidate
import ofdskit.lib.pythonvalidate
import ofdskit.lib.schema


def main():
    parser = argparse.ArgumentParser(description="OFDSKit")
    subparsers = parser.add_subparsers(dest="subparser_name")

    json_to_geojson_parser = subparsers.add_parser("jsontogeojson", aliases=["jtogj"])
    json_to_geojson_parser.add_argument(
        "inputfilename", help="File name of an input JSON data file"
    )
    json_to_geojson_parser.add_argument(
        "outputnodesfilename", help="Output filename to write Nodes GeoJSON data to"
    )
    json_to_geojson_parser.add_argument(
        "outputspansfilename", help="Output filename to write Spans GeoJSON data to"
    )

    geojson_to_json_parser = subparsers.add_parser("geojsontojson", aliases=["gjtoj"])
    geojson_to_json_parser.add_argument(
        "inputnodesfilename", help="File name of an input Nodes GeoJSON data file"
    )
    geojson_to_json_parser.add_argument(
        "inputspansfilename", help="File name of an input Spans GeoJSON data file"
    )
    geojson_to_json_parser.add_argument(
        "outputfilename", help="Output filename to write JSON data to"
    )

    json_schema_validate_parser = subparsers.add_parser(
        "jsonschemavalidate", aliases=["jsv"]
    )
    json_schema_validate_parser.add_argument(
        "inputfilename", help="File name of an input JSON data file"
    )

    python_validate_parser = subparsers.add_parser("pythonvalidate", aliases=["pv"])
    python_validate_parser.add_argument(
        "inputfilename", help="File name of an input JSON data file"
    )

    args = parser.parse_args()

    if args.subparser_name == "jsontogeojson" or args.subparser_name == "jtogj":

        with open(args.inputfilename) as fp:
            input_data = json.load(fp)

        converter = ofdskit.lib.geojson.JSONToGeoJSONConverter()
        converter.process_package(input_data)

        with open(args.outputnodesfilename, "w") as fp:
            json.dump(converter.get_nodes_geojson(), fp, indent=4)

        with open(args.outputspansfilename, "w") as fp:
            json.dump(converter.get_spans_geojson(), fp, indent=4)

    elif args.subparser_name == "geojsontojson" or args.subparser_name == "gjtoj":

        with open(args.inputnodesfilename) as fp:
            nodes_data = json.load(fp)

        with open(args.inputspansfilename) as fp:
            spans_data = json.load(fp)

        converter = ofdskit.lib.geojson.GeoJSONToJSONConverter()
        converter.process_data(nodes_data, spans_data)

        with open(args.outputfilename, "w") as fp:
            json.dump(converter.get_json(), fp, indent=4)

    elif args.subparser_name == "jsonschemavalidate" or args.subparser_name == "jsv":

        with open(args.inputfilename) as fp:
            input_data = json.load(fp)

        schema = ofdskit.lib.schema.OFDSSchema()
        validators = ofdskit.lib.jsonschemavalidate.JSONSchemaValidator(schema)

        output = validators.validate(input_data)

        output_json = [o.json() for o in output]

        print(json.dumps(output_json, indent=4))

    elif args.subparser_name == "pythonvalidate" or args.subparser_name == "pv":

        with open(args.inputfilename) as fp:
            input_data = json.load(fp)

        schema = ofdskit.lib.schema.OFDSSchema()
        validator = ofdskit.lib.pythonvalidate.PythonValidate(schema)

        output = validator.validate(input_data)

        print(json.dumps(output, indent=4))


if __name__ == "__main__":
    main()
