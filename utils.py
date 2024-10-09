import json, sys

def set_identity(name):
    identity = {"name": name}
    with open("identity.json", "w") as f:
        json.dump(identity, f, ident = 4)

def load_identity():
    try:
        with open("identity.json", "r") as f:
            identity = json.load(f)
            name = identity["name"]
            return name
    except FileNotFoundError:
        print("Please set identity and then continue.")
        sys.exit()
