from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.table.table_property_attributes import Justification
from core.ui_objects.table.validator import validate_word_table_rows
from core.ui_objects.table.validator import validate_word_table_columns


class Table(BaseContainerTag):
    def __init__(self, rows: int, cols: int):
        super().__init__()
        self.rows = validate_word_table_rows(rows)
        self.columns = validate_word_table_columns(cols)

    @property
    def tag(self):
        return "w:tbl"

    @property
    def access_children(self) -> list[dict]:
        return []

    @property
    def access_property(self) -> list[dict]:
        return [{"class": TableProperty, "required_position": 0}]


class TableProperty(BaseContainerTag):
    @property
    def tag(self):
        return "w:tblPr"

    def access_children(self) -> list[dict]:
        return [
            {"class": Justification},
        ]

    def access_property(self) -> list[dict]:
        return list()
