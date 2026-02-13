from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.base_container_tag import BaseContainerTag


class TableGrid(BaseContainerTag):
    @property
    def tag(self) -> str:
        return "w:tblGrid"

    @property
    def access_children(self) -> list[dict]:
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class GridColumn(BaseContentTag):
    """Column tag <w:gridCol> assignment"""

    __slots__ = ("_w",)

    def __init__(self, width: int):
        self.w = width

    @property
    def tag(self) -> str:
        return "w:gridCol"

    @property
    def w(self):
        pass


class W:
    pass
