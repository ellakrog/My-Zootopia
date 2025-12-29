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
    """Generates professional HTML cards for animals"""
    output = ""

    for animal in animals_data:
        output += '<li class="cards__item">\n'

        # Title (name)
        if "name" in animal:
            output += f'  <div class="card__title">{animal["name"]}</div>\n'

        output += '  <p class="card__text">\n'

        # Diet
        if "characteristics" in animal and "diet" in animal["characteristics"]:
            output += f'      <strong>Diet:</strong> {animal["characteristics"]["diet"]}<br/>\n'

        # Location
        if "locations" in animal and animal["locations"]:
            output += f'      <strong>Location:</strong> {animal["locations"][0]}<br/>\n'

        # Type
        if "characteristics" in animal and "type" in animal["characteristics"]:
            output += f'      <strong>Type:</strong> {animal["characteristics"]["type"]}<br/>\n'

        output += '  </p>\n'
        output += '</li>\n'

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

