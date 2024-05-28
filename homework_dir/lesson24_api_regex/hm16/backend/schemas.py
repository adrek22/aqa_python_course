ADD_PET = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            },
        },
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "items": {"type": "string"}
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
            }
        },
        "status": {"type": "string"}
    }
}

GET_PET = {
    "$schema": "http://json-schema.org/draft-07/schema#",
    "type": "object",
    "properties": {
        "id": {"type": "integer"},
        "category": {
            "type": "object",
            "properties": {
                "id": {"type": "integer"},
                "name": {"type": "string"}
            },
        },
        "name": {"type": "string"},
        "photoUrls": {
            "type": "array",
            "items": {"type": "string"}
        },
        "tags": {
            "type": "array",
            "items": {
                "type": "object",
                "properties": {
                    "id": {"type": "integer"},
                    "name": {"type": "string"}
                },
            }
        },
        "status": {"type": "string"}
    }
}

DELETE_PET = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'code': {'type': 'integer'},
        'type': {'type': 'string'},
        'message': {'type': 'string'}
    },
    'required': ['code', 'message', 'type']
}

ERROR = {
    '$schema': 'http://json-schema.org/draft-07/schema#',
    'type': 'object',
    'properties': {
        'code': {'type': 'integer'},
        'type': {'type': 'string'},
        'message': {'type': 'string'}
    },
    'required': ['code', 'message', 'type']
}
