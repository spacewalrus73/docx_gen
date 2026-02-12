from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.paragraph import Paragraph


class TableCellProperty(BaseContainerTag):
    pass


class TableCell(BaseContainerTag):
    @property
    def tag(self) -> str:
        return "w:tc"

    @property
    def access_children(self) -> list[dict]:
        return [{"class": Paragraph}]

    @property
    def access_property(self) -> list[dict]:
        return [{"class": TableCellProperty, "required_position": 0}]
