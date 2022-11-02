from jsonschema.exceptions import ValidationError as JSONSchemaExceptionsValidationError
from jsonschema.validators import Draft202012Validator

from ofdskit.lib.schema import OFDSSchema


class JSONSchemaValidator:
    def __init__(self, schema: OFDSSchema):
        self._schema = schema

    def validate(self, json_data: dict) -> list:
        validator = Draft202012Validator(schema=self._schema.get_schema())
        output = []
        for e in validator.iter_errors(json_data):
            output.append(ValidationError(e))
        return output


class ValidationError:
    def __init__(
        self,
        json_schema_exceptions_validation_error: JSONSchemaExceptionsValidationError,
    ):
        self._message = json_schema_exceptions_validation_error.message
        self._path = json_schema_exceptions_validation_error.path
        self._schema_path = json_schema_exceptions_validation_error.schema_path
        self._validator = json_schema_exceptions_validation_error.validator

    def json(self):
        return {
            "message": self._message,
            "path": list(self._path),
            "schema_path": list(self._schema_path),
            "validator": self._validator,
        }
