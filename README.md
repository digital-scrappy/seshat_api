# Seshat API

This is the Python binding for the Seshat API. The Seshat API is a RESTful API
that allows you to interact with the Seshat database. The Seshat database is a
database of historical and archaeological data. The Seshat API allows you to
query the database and retrieve data in a structured format.

## Installation

To install the Seshat API, you can use pip:

```bash
git clone https://github.com/Seshat-Global-History-Databank/seshat_api
cd seshat_api
pip install .
```

## Usage

To use the Seshat API, you need to create a `SeshatAPI` client object and use
it to interact with the database.

The best way to get started is to try one of our [example notebooks](examples/), which demo how to use the package.

### Quick start

Here is an example of how to set up a client:

```python
from seshat_api import SeshatAPI

# Set up a client
client = SeshatAPI(username="<USERNAME>", password="<PASSWORD>")
```

Here is an example of how to use the API to retrieve data from the database:

```python
# Get all the polities in the database
from seshat_api.core import Polities

polities = Polities(client)

# Show me how many polities are in the database
print(len(polities))

# Iterate through the polities
for polity in polities:
    print(polity.id, polity.name)
```

## Documentation

Documentation for the Seshat project can be found at [seshat-global-history-databank.github.io](https://seshat-global-history-databank.github.io/seshat/index.html).

*🚧 Documentation specific to the Seshat API has not yet been built (a [documentation](docs) folder exists). Try one of our [example notebooks](examples/), which demo how to use the package.🚧*

## Developers

Install the developer requirements with pip:

```bash
pip install -r requirements-dev.txt
nbstripout --install
pre-commit install
```

## License

This project is licensed under the MIT License - see the [LICENSE](LICENSE)
file for details.
