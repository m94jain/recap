import pandera as pa
from pandera.typing import Index, DataFrame, Series


from recap.schema import model


def from_pandera(
    pandera_schema: pa.DataFrameSchema,
) -> model.StructSchema:
    fields = []

    for column in pandera_schema.columns:
        match str.lower(pandera_schema.columns[column].dtype.type.name):
            case "int64":
                SchemaClass = model.Int64Schema
            case "float64":
                SchemaClass = model.Float64Schema
            case "bool":
                SchemaClass = model.BooleanSchema
            case "str":
                SchemaClass = model.StringSchema
            case "datetime64":
                SchemaClass = model.TimestampSchema
            case "datetime64[ns]":
                SchemaClass = model.TimestampSchema
            case "int32":
                SchemaClass = model.Int32Schema
            case "float32":
                SchemaClass = model.Float32Schema
            case "int16":
                SchemaClass = model.Int16Schema
            case "int8":
                SchemaClass = model.Int8Schema
            case "object":
                SchemaClass = model.StringSchema
            case "timedelta64[ns]":
                SchemaClass = model.TimeSchema
            case _:
                raise ValueError(
                    "Can't convert to Recap type from Pandera "
                    f"type={pandera_schema.columns[column].dtype}"
                )
        fields.append(
            model.Field(
                name=column,
                schema=SchemaClass(
                    doc=pandera_schema.columns[column].description,
                    optional=pandera_schema.columns[column].required
                ),
            )
        )
    return model.StructSchema(fields=fields, optional=False)
