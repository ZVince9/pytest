# This is python based automation test suite which will include
- test_ui - made using pw
- test_api - made using simple api requests

## Getting Started

Make sure you setup virtual env and activate it:

- `python3 -m venv pytest-env`
- `source pytest-env/bin/activate`

Install needed dependencies:

`pip install -r requirements.txt`


## To run the tests

- `pytest`
- `pytest -v` - to see nicer output
- `pytest -m login -v` - to run with specific mark
- `pytest -n 3` - to run with more workers defined [3]
