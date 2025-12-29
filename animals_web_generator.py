import json


def load_data(file_path):
    """Loads a JSON file"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return json.load(handle)


def load_template(file_path):
    """Loads HTML template"""
    with open(file_path, "r", encoding="utf-8") as handle:
        return handle.read()


def generate_animals_info(animals_data):
    """Generates string with animals data"""
    output = ""

    for animal in animals_data:

        if "name" in animal:
            output += f"Name: {animal['name']}\n"

        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f"Diet: {animal['characteristics']['diet']}\n"

        if "locations" in animal and animal["locations"]:
            output += f"Location: {animal['locations'][0]}\n"

        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f"Type: {animal['characteristics']['type']}\n"

        output += "\n"  # prazna linija između životinja

    return output


def main():
    animals_data = load_data("animals_data.json")
    template = load_template("animals_template.html")

    animals_info = generate_animals_info(animals_data)

    final_html = template.replace("__REPLACE_ANIMALS_INFO__", animals_info)

    with open("animals.html", "w", encoding="utf-8") as handle:
        handle.write(final_html)


if __name__ == "__main__":
    main()

