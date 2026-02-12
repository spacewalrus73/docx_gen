from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.table.cell import TableCell


class TableRowProperty(BaseContainerTag):
    pass


class TableRow(BaseContainerTag):
    @property
    def tag(self):
        return "w:tr"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": TableCell}]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": TableRowProperty, "required_position": 0}]

    def add_cell(self):
        self.add(TableCell())
