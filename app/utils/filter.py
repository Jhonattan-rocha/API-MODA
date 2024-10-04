from app.Mapping import models_mapping
from sqlalchemy.types import Integer, String, Float, Boolean, Date, DateTime
from sqlalchemy import and_, func, Column


def convert_to_column_type(column, value):
    column_type = column.type

    try:
        if isinstance(column_type, Integer):
            return int(value)
        elif isinstance(column_type, Float):
            return float(value)
        elif isinstance(column_type, Boolean):
            return value.lower() in ['true', '1', 'yes']
        elif isinstance(column_type, Date) or isinstance(column_type, DateTime):
            from datetime import datetime
            return datetime.fromisoformat(value)
        elif isinstance(column_type, String):
            return str(value)
        else:
            return value  # Fallback: tenta usar o valor como está
    except (ValueError, TypeError):
        raise ValueError(f"Invalid value '{value}' for column type {column_type}")


def apply_filters_dynamic(query, filters, model):
    conditions = []
    db_model = models_mapping[model]
    filters = filters.split("$")
    for filter_string in filters:
        aux = filter_string.split("+")

        if len(aux) == 3:
            field, operator, value = aux
            column: Column = getattr(db_model, field)

            try:
                value = convert_to_column_type(column, value)
            except ValueError as e:
                continue

            if operator == "eq":  # equals
                conditions.append(column == value)
            elif operator == "ne":  # not equals
                conditions.append(column != value)
            elif operator == "lt":  # less than
                conditions.append(column < value)
            elif operator == "le":  # less than or equal to
                conditions.append(column <= value)
            elif operator == "gt":  # greater than
                conditions.append(column > value)
            elif operator == "ge":  # greater than or equal to
                conditions.append(column >= value)
            elif operator == "ct":  # contains
                conditions.append(func.lower(column).like(f"%{value}%".lower()))
            elif operator == "sw":  # starts with
                conditions.append(func.lower(column).like(f"{value}%".lower()))
            elif operator == "ew":  # ends with
                conditions.append(func.lower(column).like(f"%{value}".lower()))
            elif operator == "in":
                conditions.append(column.in_([convert_to_column_type(column, val) for val in str(value).split(',')]))
        if len(aux) == 2:
            constraint, column = aux

            if constraint == 'order_by':
                query = query.order_by(column if column else None)
    if conditions:
        query = query.where(and_(*conditions))

    return query
