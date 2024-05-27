from jsonschema import validate


def validate_schema(json_response: dict, expected_schema: dict):
    validate(json_response, expected_schema)