import json

def get_cctv_summary():

    with open("data/cctv_summary.json") as f:
        data = json.load(f)

    return data