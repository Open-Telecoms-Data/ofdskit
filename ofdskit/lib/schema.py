import requests


class OFDSSchema:

    url: str = "https://raw.githubusercontent.com/Open-Telecoms-Data/open-fibre-data-standard/b2b4ed722d6b078251da05eb0da8304ebefd34e5/schema/network-package-schema.json"

    def get_schema(self):
        r = requests.get(self.url)
        return r.json()

    def extract_data_ids_from_data_and_path(self, data: dict, path: list) -> dict:
        out: dict = {}
        # network_id
        if len(path) >= 2 and path[0] == "networks":
            network_id = data["networks"][path[1]].get("id")
            if network_id:
                out["network_id"] = network_id
        # other ids
        for field in ["node", "span"]:
            if len(path) >= 4 and path[0] == "networks" and path[2] == field + "s":
                id = data["networks"][path[1]][field + "s"][path[3]].get("id")
                if id:
                    out[field + "_id"] = id
        # return
        return out
