from core.ui_objects.base.base_container_tag import BaseContainerTag
from core.ui_objects.base.base_content_tag import BaseContentTag
from core.ui_objects.base.linked_objects import Objects
from core.ui_objects.atrib.margins import DistTop, DistRight, DistLeft, DistBottom
from core.ui_objects.atrib.ids import AnchorId, EditId
import uuid
from core.utils.metrics import Cm
from core.ui_objects.atrib.size import CX, CY
from core.ui_objects.atrib.size import EffectLeft, EffectRight, EffectTop, EffectBottom
from core.ui_objects.atrib.image.image import (
    ImageName,
    ImageHidden,
    ImageDescr,
    ImageId,
    ImageTitle
)
from core.ui_objects.atrib.image.graphic_frame_locks import (
    NoChangeAspect,
    NoChangeArrowheads,
    NoEditPoints,
    NoAdjustHandles,
    NoChangeShapeType,
    NoChangeStart,
    NoChangeEnd,
    NoMove,
    NoResize,
    NoRotate,
    NoSelect,
    NoCrop,
    NoChangeBullet,
    NoGrp,
    NoUngrp,
    NoDrilldown,
    NoTextEdit,
    GraphicFrameLocksNS,
)
from core.ui_objects.atrib.image.image import URIGraphicData
from core.ui_objects.atrib.image.CNvPr import (
    ObjectName,
    ObjectHidden,
    ObjectId,
    ObjectDescr,
    ObjectTitle
)


class Inline(BaseContainerTag):
    _slots__ = ("_objects", "_property", "_distT", "_distB", "_distL", "_distR", "_")

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)
        self._distT = DistTop(0)
        self._distB = DistBottom(0)
        self._distL = DistLeft(0)
        self._distR = DistRight(0)
        self._anchorId = AnchorId(self.generate_random_id())
        self._editId = EditId(self.generate_random_id())

    @property
    def dist_top(self):
        return self._distT.value

    @dist_top.setter
    def dist_top(self, value):
        """take value in centimeters"""

        self._distT.value = Cm(value)

    @property
    def dist_bottom(self):
        return self._distB.value

    @dist_bottom.setter
    def dist_bottom(self, value):
        """take value in centimeters"""

        self._distB.value = Cm(value)

    @property
    def dist_left(self):
        return self._distL.value

    @dist_left.setter
    def dist_left(self, value):
        """take value in centimeters"""

        self._distL.value = Cm(value)

    @property
    def dist_right(self):
        return self._distR.value

    @dist_right.setter
    def dist_right(self, value):
        """take value in centimeters"""

        self._distR.value = Cm(value)

    @property
    def anchor_id(self):
        """wp14:anchorId"""
        return self._anchorId.value

    @anchor_id.setter
    def anchor_id(self, value):
        self._anchorId.value = value

    @property
    def edit_id(self):
        """wp14:editId"""

        return self._editId.value

    @edit_id.setter
    def edit_id(self, value):
        self._editId.value = value

    def set_distances(self, top=0, bottom=0, left=0, right=0):
        """Установить все отступы одновременно"""

        self.dist_top = top
        self.dist_bottom = bottom
        self.dist_left = left
        self.dist_right = right

    def set_all_distances(self, value):
        """Установить одинаковые отступы со всех сторон"""

        self.dist_top = value
        self.dist_bottom = value
        self.dist_left = value
        self.dist_right = value

    @staticmethod
    def generate_random_id():
        """Сгенерировать случайный Id"""

        return uuid.uuid4().hex[:8].upper()

    @property
    def tag(self):
        return "wp:inline"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class Extent(BaseContentTag):
    __slots__ = ("_width", "_height")

    def __init__(self):
        self._width = CX(Cm(21))
        self._height = CY(Cm(11))

    @property
    def width(self):
        return self._width.value

    @width.setter
    def width(self, value):
        """take value in centimeters"""

        self._width.value = Cm(value)

    @property
    def height(self):
        return self._height.value

    @height.setter
    def height(self, value):
        """take value in centimeters"""

        self._height.value = Cm(value)

    def set_distances(self, width=10, height=10):
        """Установить все отступы одновременно"""
        self.width = width
        self.height = height

    @property
    def tag(self) -> str:
        return "wp:extent"


class EffectExtent(BaseContentTag):
    """Класс для тега <wp:effectExtent>"""

    __slots__ = ("_left", "_top", "_right", "_bottom")

    def __init__(self):
        self._left = EffectLeft(Cm(0))
        self._top = EffectTop(Cm(0))
        self._right = EffectRight(Cm(0))
        self._bottom = EffectBottom(Cm(0))

    @property
    def left(self):
        return self._left

    @left.setter
    def left(self, value):
        self._left.value = Cm(value)

    @property
    def top(self):
        return self._top

    @top.setter
    def top(self, value):
        self._top.value = Cm(value)

    @property
    def right(self):
        return self._right

    @right.setter
    def right(self, value):
        self._right.value = Cm(value)

    @property
    def bottom(self):
        return self._bottom

    @bottom.setter
    def bottom(self, value):
        self._bottom.value = Cm(value)

    @property
    def tag(self):
        return "wp:effectExtent"


class DocProperties(BaseContentTag):
    """Класс для тега <wp:docPr> (Document Properties)"""
    __slots__ = ("_id", "_name", "_description", "_title", "_hidden")

    def __init__(self):
        self._id = ImageId(0)
        self._name = ImageName("")
        self._description = ImageDescr("")
        self._title = ImageTitle("")
        self._hidden = ImageHidden("0")

    @property
    def id(self) -> int:
        """Уникальный идентификатор объекта"""
        return self._id.value

    @id.setter
    def id(self, value: int):
        if not isinstance(value, int) or value < 1:
            raise ValueError("ID должен быть положительным целым числом")
        self._id.value = value

    @property
    def name(self) -> str:
        """Отображаемое имя объекта"""
        return self._name.value

    @name.setter
    def name(self, value: str):
        self._name.value = str(value)

    @property
    def description(self) -> str:
        """Описание объекта (альтернативный текст)"""
        return self._description.value

    @description.setter
    def description(self, value: str):
        self._description.value = str(value)

    @property
    def title(self) -> str:
        """Заголовок (всплывающая подсказка)"""
        return self._title.value

    @title.setter
    def title(self, value: str):
        self._title.value = str(value)

    @property
    def hidden(self) -> bool:
        """Скрыт ли объект?"""
        return self._hidden.value

    @hidden.setter
    def hidden(self, value: bool):
        self._hidden.value = "1" if value else "0"

    @property
    def tag(self):
        return "wp:docPr"

    def __str__(self):
        return f"DocPr(id={self.id}, name='{self.name}')"


class CNvGraphicFramePr(BaseContainerTag):
    """
    Non-Visual Properties for a Graphic Frame
    Содержит свойства, которые не влияют на отображение графического фрейма
    """
    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "wp:cNvGraphicFramePr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class GraphicFrameLocks(BaseContentTag):
    """
    DrawingML Graphic Frame Locks
    Блокировки для графического фрейма
    """
    __slots__ = (
        "_no_change_aspect", "_no_change_arrowheads",
        "_no_change_start", "_no_change_end", "_no_edit_points",
        "_no_adjust_handles", "_no_change_shape_type", "_no_move",
        "_no_resize", "_no_rotate", "_no_select", "_no_crop", "_no_change_bullet",
        "_no_grp", "_no_ungrp", "_no_drill_down", "_no_text_edit"
    )

    def __init__(self):
        """Блокировка изменения пропорций (1 = да, 0 = нет)"""

        self.no_change_aspect = NoChangeAspect("0")
        self.no_change_arrowheads = NoChangeArrowheads("0")
        self.no_change_start = NoChangeStart("0")
        self.no_change_end = NoChangeEnd("0")
        self.no_edit_points = NoEditPoints("0")
        self.no_adjust_handles = NoAdjustHandles("0")
        self.no_change_shape_type = NoChangeShapeType("0")
        self.no_change_shape_type = NoChangeShapeType("0")
        self.no_move = NoMove("0")
        self.no_resize = NoResize("0")
        self.no_rotate = NoRotate("0")
        self.no_select = NoSelect("0")
        self.no_crop = NoCrop("0")
        self.no_change_bullet = NoChangeBullet("0")
        self.no_grp = NoGrp("0")
        self.no_ungrp = NoUngrp("0")
        self.no_drill_down = NoDrilldown("0")
        self.no_text_edit = NoTextEdit("0")
        self.xmlns = GraphicFrameLocksNS("")

    @property
    def no_change_aspect(self):
        return self._no_change_aspect.value

    @no_change_aspect.setter
    def no_change_aspect(self, value: bool):
        self._no_change_aspect.value = "1" if value else "0"

    @property
    def no_change_arrowheads(self):
        return self._no_change_arrowheads.value

    @no_change_arrowheads.setter
    def no_change_arrowheads(self, value: bool):
        self._no_change_arrowheads.value = "1" if value else "0"

    @property
    def no_change_start(self):
        """Блокировка изменения начальной точки"""
        return self._no_change_start.value

    @no_change_start.setter
    def no_change_start(self, value: bool):
        self._no_change_start.value = "1" if value else "0"

    @property
    def no_change_end(self):
        """Блокировка изменения конечной точки"""
        return self._no_change_end.value

    @no_change_end.setter
    def no_change_end(self, value: bool):
        self._no_change_end.value = "1" if value else "0"

    @property
    def no_edit_points(self):
        """Запрет редактирования точек"""
        return self._no_edit_points.value

    @no_edit_points.setter
    def no_edit_points(self, value: bool):
        self._no_edit_points.value = "1" if value else "0"

    @property
    def no_adjust_handles(self):
        """Запрет изменения ручек настройки"""
        return self._no_adjust_handles

    @no_adjust_handles.setter
    def no_adjust_handles(self, value: bool):
        self._no_adjust_handles.value = "1" if value else "0"

    @property
    def no_change_shape_type(self):
        """Запрет изменения типа фигуры"""
        return self._no_change_shape_type.value

    @no_change_shape_type.setter
    def no_change_shape_type(self, value: bool):
        self._no_change_shape_type.value = "1" if value else "0"

    @property
    def no_move(self):
        """Запрет перемещения"""
        return self._no_move.value

    @no_move.setter
    def no_move(self, value: bool):
        self._no_move.value = "1" if value else "0"

    @property
    def no_resize(self):
        """Запрет изменения размера"""
        return self._no_resize.value

    @no_resize.setter
    def no_resize(self, value: bool):
        self._no_resize.value = "1" if value else "0"

    @property
    def no_rotate(self):
        """Запрет вращения"""
        return self._no_rotate.value

    @no_rotate.setter
    def no_rotate(self, value: bool):
        self._no_rotate.value = "1" if value else "0"

    @property
    def no_select(self):
        """Запрет выделения"""
        return self._no_select.value

    @no_select.setter
    def no_select(self, value: bool):
        self._no_select.value = "1" if value else "0"

    @property
    def no_crop(self):
        """Запрет обрезки"""
        return self._no_crop.value

    @no_crop.setter
    def no_crop(self, value: bool):
        self._no_crop.value = "1" if value else "0"

    @property
    def no_change_bullet(self):
        """Запрет обрезки"""
        return self._no_change_bullet.value

    @no_change_bullet.setter
    def no_change_bullet(self, value: bool):
        self._no_change_bullet.value = "1" if value else "0"

    @property
    def no_grp(self):
        """Запрет обрезки"""
        return self._no_grp.value

    @no_grp.setter
    def no_grp(self, value: bool):
        self._no_grp.value = "1" if value else "0"

    @property
    def no_ungrp(self):
        """Запрет обрезки"""
        return self._no_ungrp.value

    @no_ungrp.setter
    def no_ungrp(self, value: bool):
        self._no_ungrp.value = "1" if value else "0"

    @property
    def no_drill_down(self):
        """Запрет обрезки"""
        return self._no_drill_down.value

    @no_drill_down.setter
    def no_drill_down(self, value: bool):
        self._no_drill_down.value = "1" if value else "0"

    @property
    def no_text_edit(self):
        """Запрет обрезки"""
        return self._no_text_edit.value

    @no_text_edit.setter
    def no_text_edit(self, value: bool):
        self._no_text_edit.value = "1" if value else "0"

    @property
    def xmlns(self):
        """Запрет обрезки"""
        return self._xmlns.value

    @xmlns.setter
    def xmlns(self, value: str):
        self._xmlns.value = value

    @property
    def tag(self) -> str:
        return "a:graphicFrameLocks"

    def lock_all(self):
        """Заблокировать все изменения"""
        self.no_change_aspect.value = 1
        self.no_change_arrowheads.value = 1
        self.no_change_start.value = 1
        self.no_change_end.value = 1
        self.no_edit_points.value = 1
        self.no_adjust_handles.value = 1
        self.no_change_shape_type.value = 1
        self.no_move.value = 1
        self.no_resize.value = 1
        self.no_rotate.value = 1
        self.no_select.value = 1
        self.no_crop.value = 1

    def unlock_all(self):
        """Разблокировать все изменения"""
        self.no_change_aspect.value = 0
        self.no_change_arrowheads.value = 0
        self.no_change_start.value = 0
        self.no_change_end.value = 0
        self.no_edit_points.value = 0
        self.no_adjust_handles.value = 0
        self.no_change_shape_type.value = 0
        self.no_move.value = 0
        self.no_resize.value = 0
        self.no_rotate.value = 0
        self.no_select.value = 0
        self.no_crop.value = 0


class Graphic(BaseContainerTag):
    """
    DrawingML Graphic element
    Основной контейнер для графических данных
    """
    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:graphic"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class GraphicData(BaseContainerTag):
    """
    DrawingML Graphic Data element
    Содержит графические данные с указанием типа
    """
    __slots__ = ("_uri",)

    def __init__(self, objects: Objects | list = None, uri: str = None):
        super().__init__(objects)
        self._uri = URIGraphicData(URIGraphicData.Options.pic.value)

    @property
    def uri(self) -> str:
        """URI типа графических данных"""
        return self._uri.value

    @uri.setter
    def uri(self, value: str):
        self._uri = str(value)

    @property
    def tag(self):
        return "a:graphicData"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        """Генерация XML атрибутов"""
        if self._uri:
            return [{"uri": self._uri}]
        return []


class Pic(BaseContainerTag):
    """
    Picture element - основной контейнер для изображения
    Содержит все компоненты изображения
    """
    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:pic"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class NvPicPr(BaseContainerTag):
    """
    Non-Visual Picture Properties
    Свойства изображения, не влияющие на отображение
    """
    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:nvPicPr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class CNvPr(BaseContentTag):
    """
    Common Non-Visual Drawing Properties
    Общие свойства для всех графических объектов
    """
    __slots__ = ("_id", "_name", "_description", "_title", "_hidden")

    def __init__(self):
        self.id = ObjectId(0)
        self.name = ObjectName("")
        self.description = ObjectDescr("")
        self.title = ObjectTitle("")
        self.hidden = ObjectHidden(ObjectHidden.Options.visible.value)

    @property
    def id(self) -> int:
        """Идентификатор объекта"""
        return self._id.value

    @id.setter
    def id(self, value: int):
        self._id.value = int(value)

    @property
    def name(self) -> str:
        """Имя объекта"""
        return self._name.value

    @name.setter
    def name(self, value: str):
        self._name.value = str(value)

    @property
    def description(self) -> str:
        """Описание (альтернативный текст)"""
        return self._description.value

    @description.setter
    def description(self, value: str):
        self._description.value = str(value)

    @property
    def title(self) -> str:
        """Заголовок (всплывающая подсказка)"""
        return self._title.value

    @title.setter
    def title(self, value: str):
        self._title.value = str(value)

    @property
    def hidden(self) -> bool:
        """Скрыт ли объект?"""
        return self._hidden.value

    @hidden.setter
    def hidden(self, value: bool):
        self._hidden.value = bool(value)

    @property
    def tag(self) -> str:
        return "pic:cNvPr"




class CNvPicPr(BaseContainerTag):
    """
    Non-Visual Picture Properties
    Специфические свойства для изображений
    """
    __slots__ = ()

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:cNvPicPr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class PicLocks(BaseContentTag):
    __slots__ = (
        "_no_change_aspect", "_no_change_arrowheads",
        "_no_change_start", "_no_change_end", "_no_edit_points",
        "_no_adjust_handles", "_no_change_shape_type", "_no_move",
        "_no_resize", "_no_rotate", "_no_select", "_no_crop", "_no_change_bullet",
        "_no_grp", "_no_ungrp", "_no_drill_down", "_no_text_edit"
    )

    def __init__(self):
        """Блокировка изменения пропорций (1 = да, 0 = нет)"""

        self.no_change_aspect = NoChangeAspect("0")
        self.no_change_arrowheads = NoChangeArrowheads("0")
        self.no_change_start = NoChangeStart("0")
        self.no_change_end = NoChangeEnd("0")
        self.no_edit_points = NoEditPoints("0")
        self.no_adjust_handles = NoAdjustHandles("0")
        self.no_change_shape_type = NoChangeShapeType("0")
        self.no_change_shape_type = NoChangeShapeType("0")
        self.no_move = NoMove("0")
        self.no_resize = NoResize("0")
        self.no_rotate = NoRotate("0")
        self.no_select = NoSelect("0")
        self.no_crop = NoCrop("0")
        self.no_change_bullet = NoChangeBullet("0")
        self.no_grp = NoGrp("0")
        self.no_ungrp = NoUngrp("0")
        self.no_drill_down = NoDrilldown("0")
        self.no_text_edit = NoTextEdit("0")
        self.xmlns = GraphicFrameLocksNS("")

    @property
    def no_change_aspect(self):
        return self._no_change_aspect.value

    @no_change_aspect.setter
    def no_change_aspect(self, value: bool):
        self._no_change_aspect.value = "1" if value else "0"

    @property
    def no_change_arrowheads(self):
        return self._no_change_arrowheads.value

    @no_change_arrowheads.setter
    def no_change_arrowheads(self, value: bool):
        self._no_change_arrowheads.value = "1" if value else "0"

    @property
    def no_change_start(self):
        """Блокировка изменения начальной точки"""
        return self._no_change_start.value

    @no_change_start.setter
    def no_change_start(self, value: bool):
        self._no_change_start.value = "1" if value else "0"

    @property
    def no_change_end(self):
        """Блокировка изменения конечной точки"""
        return self._no_change_end.value

    @no_change_end.setter
    def no_change_end(self, value: bool):
        self._no_change_end.value = "1" if value else "0"

    @property
    def no_edit_points(self):
        """Запрет редактирования точек"""
        return self._no_edit_points.value

    @no_edit_points.setter
    def no_edit_points(self, value: bool):
        self._no_edit_points.value = "1" if value else "0"

    @property
    def no_adjust_handles(self):
        """Запрет изменения ручек настройки"""
        return self._no_adjust_handles

    @no_adjust_handles.setter
    def no_adjust_handles(self, value: bool):
        self._no_adjust_handles.value = "1" if value else "0"

    @property
    def no_change_shape_type(self):
        """Запрет изменения типа фигуры"""
        return self._no_change_shape_type.value

    @no_change_shape_type.setter
    def no_change_shape_type(self, value: bool):
        self._no_change_shape_type.value = "1" if value else "0"

    @property
    def no_move(self):
        """Запрет перемещения"""
        return self._no_move.value

    @no_move.setter
    def no_move(self, value: bool):
        self._no_move.value = "1" if value else "0"

    @property
    def no_resize(self):
        """Запрет изменения размера"""
        return self._no_resize.value

    @no_resize.setter
    def no_resize(self, value: bool):
        self._no_resize.value = "1" if value else "0"

    @property
    def no_rotate(self):
        """Запрет вращения"""
        return self._no_rotate.value

    @no_rotate.setter
    def no_rotate(self, value: bool):
        self._no_rotate.value = "1" if value else "0"

    @property
    def no_select(self):
        """Запрет выделения"""
        return self._no_select.value

    @no_select.setter
    def no_select(self, value: bool):
        self._no_select.value = "1" if value else "0"

    @property
    def no_crop(self):
        """Запрет обрезки"""
        return self._no_crop.value

    @no_crop.setter
    def no_crop(self, value: bool):
        self._no_crop.value = "1" if value else "0"

    @property
    def no_change_bullet(self):
        """Запрет обрезки"""
        return self._no_change_bullet.value

    @no_change_bullet.setter
    def no_change_bullet(self, value: bool):
        self._no_change_bullet.value = "1" if value else "0"

    @property
    def no_grp(self):
        """Запрет обрезки"""
        return self._no_grp.value

    @no_grp.setter
    def no_grp(self, value: bool):
        self._no_grp.value = "1" if value else "0"

    @property
    def no_ungrp(self):
        """Запрет обрезки"""
        return self._no_ungrp.value

    @no_ungrp.setter
    def no_ungrp(self, value: bool):
        self._no_ungrp.value = "1" if value else "0"

    @property
    def no_drill_down(self):
        """Запрет обрезки"""
        return self._no_drill_down.value

    @no_drill_down.setter
    def no_drill_down(self, value: bool):
        self._no_drill_down.value = "1" if value else "0"

    @property
    def no_text_edit(self):
        """Запрет обрезки"""
        return self._no_text_edit.value

    @no_text_edit.setter
    def no_text_edit(self, value: bool):
        self._no_text_edit.value = "1" if value else "0"

    @property
    def xmlns(self):
        """Запрет обрезки"""
        return self._xmlns.value

    @xmlns.setter
    def xmlns(self, value: str):
        self._xmlns.value = value


    def lock_all(self):
        """Заблокировать все изменения"""
        self.no_change_aspect.value = 1
        self.no_change_arrowheads.value = 1
        self.no_change_start.value = 1
        self.no_change_end.value = 1
        self.no_edit_points.value = 1
        self.no_adjust_handles.value = 1
        self.no_change_shape_type.value = 1
        self.no_move.value = 1
        self.no_resize.value = 1
        self.no_rotate.value = 1
        self.no_select.value = 1
        self.no_crop.value = 1

    def unlock_all(self):
        """Разблокировать все изменения"""
        self.no_change_aspect.value = 0
        self.no_change_arrowheads.value = 0
        self.no_change_start.value = 0
        self.no_change_end.value = 0
        self.no_edit_points.value = 0
        self.no_adjust_handles.value = 0
        self.no_change_shape_type.value = 0
        self.no_move.value = 0
        self.no_resize.value = 0
        self.no_rotate.value = 0
        self.no_select.value = 0
        self.no_crop.value = 0

    @property
    def tag(self) -> str:
        return "a:picLocks"

# todo тут я

class BlipFill(BaseContainerTag):
    "pic:blipFill"

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:blipFill"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class Blip(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:blip"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class ExtLst(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:extLst"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class Ext(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:ext"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class UseLocalDpi(BaseContentTag):
    __slots__ = ("_type", "_clear")

    def __init__(self, type: TypeSpec = None, clear: ClearSpec = None):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return "a14:useLocalDpi"


class SrcRect(BaseContentTag):
    "a:srcRect"
    __slots__ = ("_type", "_clear")

    def __init__(self, type: TypeSpec = None, clear: ClearSpec = None):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return "a:srcRect"


class Stretch(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:stretch"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class FillRect(BaseContentTag):
    ""
    __slots__ = ("_type", "_clear")

    def __init__(self, type: TypeSpec = None, clear: ClearSpec = None):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return "a:fillRect"


class SpPr(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "pic:spPr"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class Xfrm(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:xfrm"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class Off(BaseContentTag):
    ""
    __slots__ = ("_type", "_clear")

    def __init__(self, type: TypeSpec = None, clear: ClearSpec = None):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return "a:off"


class PrstGeom(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:prstGeom"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class avLst(BaseContentTag):
    ""
    __slots__ = ("_type", "_clear")

    def __init__(self, type: TypeSpec = None, clear: ClearSpec = None):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return "a:avLst"


class NoFill(BaseContentTag):
    "a:noFill"
    __slots__ = ("_type", "_clear")

    def __init__(self, type: TypeSpec = None, clear: ClearSpec = None):
        self.clear = clear
        self.type = type

    @property
    def tag(self) -> str:
        return "a:noFill"


class Ln(BaseContainerTag):
    ""

    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "a:ln"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []


class Drawing(BaseContainerTag):
    def __init__(self, objects: Objects | list = None):
        super().__init__(objects)

    @property
    def tag(self):
        return "w:drawing"

    @property
    def access_children(self):
        return []

    @property
    def access_property(self) -> list[dict]:
        return []
