# Cycle_pricing App

This is a command line Application, which is used to generate the Bill of a Cycle by Mentioning it's configuration in a ``JSON`` file.

It uses 10 ``Threads`` to perform the operation and a blocking ``Queue``

This application also supports the configuration of Price for each part according to bill date. [Click here](#Price) to see how.

## Arguments

The application supports following commands.
* ``--configfile [json file path]``
* ``--availableparts``

### ``--configfile`` usage:
This argument will start the generation of bill for each configuration.
This is a required argument if no other argument is passed.
```sh
python Main.py --configfile /Path/to/file.json
```

### ``--availableparts`` usage:
This argument will display the list of all available components and their respective parts.
This is a required argument if no other argument is passed.
```sh
python Main.py --availableparts
```


## Input Configuration

Input is provided by using ``--configfile`` command line argument.
This argument expects a ``JSON`` file path.

### JSON Structure

Below is example of input ``JSON`` structure.

> **_NOTE:_**  *The date should always be given in "DD.MM.YYYY" format*

```json
[
  {
    "bill_date": "22.02.2005",
    "frame": "Steel",
    "handle": "Steel",
    "seat": "RacingSeat",
    "wheel": "Tubeless",
    "chain": "SixGears"
  },
  {
    "bill_date": "DD.MM.YYYY",
    "frame": "select from options ...",
    "handle": "select from options ...",
    "seat": "select from options ...",
    "wheel": "select from options ...",
    "chain": "select from options ...",
  }
]
```

## Price
All of the prices are configured in their respective ``.ini``. file,
Following is the diectory structure where all ``.ini`` files are stored.
``cycle/Components/Parts_pricing``
```
.
├── Chain
│   ├── FourGears.ini
│   ├── SixGears.ini
│   └── TwoGears.ini
├── Frame
│   ├── Aluminium.ini
│   ├── CarbonFiber.ini
│   └── Steel.ini
├── Handle
│   ├── Aluminium.ini
│   ├── CarbonFiber.ini
│   └── Steel.ini
├── Seat
│   ├── ComfortSeat.ini
│   └── RacingSeat.ini
└── Wheel
    ├── OffRoad.ini
    ├── Racing.ini
    └── Tubeless.ini
```

### INI file structure:
Each ``.ini`` file is configured as below example.
```ini
[22.02.2000-10.10.2010]
Price=700
[11.10.2010-latest]
Price=650
```
Each main section contains the range of date in ``DD.MM.YYYY`` format,
Price of each part is decided by bill date.

> **_NOTE:_**  The ``latest`` keyword in date range is replaced by ``current system date`` and then used further.

## INput JSON schema for reference:

```json
{
    "$schema": "http://json-schema.org/draft-07/schema",
    "type": "array",
    "additionalItems": true,
    "items": {
        "$id": "#/items",
        "anyOf": [
            {
                "$id": "#/items/anyOf/0",
                "type": "object",
                "description": "This sections contains Configuration for each Cycle",
                "required": [
                    "bill_date",
                    "frame",
                    "handle",
                    "seat",
                    "wheel",
                    "chain"
                ],
                "properties": {
                    "bill_date": {
                        "$id": "#/items/anyOf/0/properties/bill_date",
                        "type": "string",
                        "title": "The bill_date",
                        "description": "bill_date should always be in DD.MM.YYYY format"
                    },
                    "frame": {
                        "$id": "#/items/anyOf/0/properties/frame",
                        "type": "string",
                        "title": "The frame",
                        "description": "Type of frame"
                    },
                    "handle": {
                        "$id": "#/items/anyOf/0/properties/handle",
                        "type": "string",
                        "title": "The handle",
                        "description": "Type of handle"
                    },
                    "seat": {
                        "$id": "#/items/anyOf/0/properties/seat",
                        "type": "string",
                        "title": "The seat",
                        "description": "Type of seat"
                    },
                    "wheel": {
                        "$id": "#/items/anyOf/0/properties/wheel",
                        "type": "string",
                        "title": "The wheel",
                        "description": "Type of wheel"
                    },
                    "chain": {
                        "$id": "#/items/anyOf/0/properties/chain",
                        "type": "string",
                        "title": "The chain",
                        "description": "Type of chain"
                    }
                },
                "additionalProperties": true
            }
        ]
    }
}
```

