from typing import Set, Any
import itertools


def write_model_files(substitutions, model_template, model_type, filename):
    model = model_template.substitute(substitutions)
    with open(
        f"./models/raw_vault/{model_type}s/{model_type}_{filename}.sql", "w"
    ) as dbt_sql_export:
        dbt_sql_export.write(model)


def create_substitution_values_template():
    return {
        "filename": None,
        "hash_key": None,
        "hubs": None,
        "hub_name": None,
        "link_name": None,
        "natural_key": None,
        "record_load_datetime": "LOAD_DATETIME",
        "record_source": "RECORD_SOURCE",
        "source_list": [],
    }


def create_set_from_list_of_lists(list_of_lists) -> Set[str]:
    return set(list(itertools.chain(*list_of_lists)))
