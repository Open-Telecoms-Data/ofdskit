import argparse
import json

import ofdskit.lib.geojson


def main():
    parser = argparse.ArgumentParser(description="OFDSKit")
    subparsers = parser.add_subparsers(dest="subparser_name")

    json_to_geojson_parser = subparsers.add_parser("jsontogeojson")
    json_to_geojson_parser.add_argument("inputfilename")
    json_to_geojson_parser.add_argument("outputnodesfilename")
    json_to_geojson_parser.add_argument("outputspansfilename")

    geojson_to_json_parser = subparsers.add_parser("geojsontojson")
    geojson_to_json_parser.add_argument("inputnodesfilename")
    geojson_to_json_parser.add_argument("inputspansfilename")
    geojson_to_json_parser.add_argument("outputfilename")

    args = parser.parse_args()

    if args.subparser_name == "jsontogeojson":

        with open(args.inputfilename) as fp:
            input_data = json.load(fp)

        converter = ofdskit.lib.geojson.JSONToGeoJSONConverter()
        converter.process_package(input_data)

        with open(args.outputnodesfilename, "w") as fp:
            json.dump(converter.get_nodes_geojson(), fp, indent=4)

        with open(args.outputspansfilename, "w") as fp:
            json.dump(converter.get_spans_geojson(), fp, indent=4)

    elif args.subparser_name == "geojsontojson":

        with open(args.inputnodesfilename) as fp:
            nodes_data = json.load(fp)

        with open(args.inputspansfilename) as fp:
            spans_data = json.load(fp)

        converter = ofdskit.lib.geojson.GeoJSONToJSONConverter()
        converter.process_data(nodes_data, spans_data)

        with open(args.outputfilename, "w") as fp:
            json.dump(converter.get_json(), fp, indent=4)


if __name__ == "__main__":
    main()
