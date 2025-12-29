import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def main():
    animals_data = load_data("animals_data.json")

    for animal in animals_data:

        # Name
        if "name" in animal:
            print(f"Name: {animal['name']}")

        # Diet (u characteristics)
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            print(f"Diet: {animal['characteristics']['diet']}")

        # Location – prvi element iz liste
        if "locations" in animal and animal["locations"]:
            print(f"Location: {animal['locations'][0]}")

        # Type (u characteristics)
        if "characteristics" in animal and "type" in animal["characteristics"]:
            print(f"Type: {animal['characteristics']['type']}")

        print()  # prazna linija


if __name__ == "__main__":
    main()
