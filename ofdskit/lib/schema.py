import requests


class OFDSSchema:

    url: str = "https://raw.githubusercontent.com/Open-Telecoms-Data/open-fibre-data-standard/b2b4ed722d6b078251da05eb0da8304ebefd34e5/schema/network-package-schema.json"

    def get_schema(self):
        r = requests.get(self.url)
        return r.json()
