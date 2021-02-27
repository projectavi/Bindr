class json:
    def write_to(data, json_filepath):
        with open(json_filepath, "w+") as f:
            json.dump(data, f)
            f.close()

    def read_from(json_filepath):
        with open(json_filepath, "r") as f:
            data = json.load(f)
            f.close()
        return data