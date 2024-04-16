
# XML Generator Utility

This Python-based utility generates XML files from a JSON specification. It allows for the creation of custom XML structures with attributes and nested elements based on the configuration defined in a JSON file. This is useful for generating test data, mockups, or any situation where XML formatted data is required.

## Features

- **Customizable XML Structures**: Define any structure with nested elements and attributes.
- **Dynamic Data Generation**: Generates random data for elements based on specified data types (integer, string, float).
- **Command Line Interface**: Easy-to-use command line interface for generating XML files.

## Prerequisites

Before you can run the XML Generator, make sure you have Python installed on your machine. The utility is compatible with Python 3.x. You can download Python [here](https://www.python.org/downloads/).

## Installation

No installation is necessary. Simply download the `generate_xml.py` script and the JSON configuration file to your local machine.

## Configuration

Prepare a JSON file based on the structure you need for your XML file. Below is a sample structure to illustrate how to configure the JSON file:

```json
{
  "root": "People",
  "records": 3,
  "fields": {
    "Person": {
      "attributes": {
        "id": "int"
      },
      "nested": {
        "Name": "string",
        "Address": {
          "nested": {
            "City": "string",
            "State": "string",
            "Country": "string"
          }
        }
      }
    }
  }
}
```

This JSON configuration will generate an XML file with a root element `People` and three `Person` elements. Each `Person` has an `id` attribute, a `Name` element, and an `Address` element with nested `City`, `State`, and `Country`.

## Usage

To use the utility, navigate to the directory containing your script and JSON file in the command line and execute the script by providing the path to the JSON configuration file and the desired output XML file name.

```bash
python generate_xml.py path_to_json_file.json output.xml
```

## Output

The utility will generate an XML file at the specified output location. The file will contain XML structured according to your JSON specification, with randomly generated data for each element as defined.

## Contributing

Contributions to this project are welcome! Please fork the repository and submit a pull request