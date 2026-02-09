from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum


class GraphicFrameLocksNS(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="title")


class NoChangeAspect(EnumAttribute):
    """Запрет изменения пропорций"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noChangeAspect")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeArrowheads(EnumAttribute):
    """Запрет изменения стрелок (для линий)"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noChangeArrowheads")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoEditPoints(EnumAttribute):
    """Запрет редактирования точек фигуры"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noEditPoints")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoAdjustHandles(EnumAttribute):
    """ Запрет изменения ручек настройки"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noAdjustHandles")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeShapeType(EnumAttribute):
    """Запрет изменения типа фигуры"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noChangeShapeType")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeStart(EnumAttribute):
    """Запрет изменения начальной точки"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noChangeStart")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeEnd(EnumAttribute):
    """Запрет изменения конечной точки"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noChangeEnd")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoMove(EnumAttribute):
    """Запрет перемещения"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noMove")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoResize(EnumAttribute):
    """Запрет изменения размера"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noResize")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoRotate(EnumAttribute):
    """Запрет вращения"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noRotate")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoSelect(EnumAttribute):
    """Запрет выделения"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noSelect")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoCrop(EnumAttribute):
    """Запрет обрезки"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noCrop")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoChangeBullet(EnumAttribute):
    """Запрет изменения маркеров (для списков)"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noChangeBullet")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoGrp(EnumAttribute):
    """Запрет группировки"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noGrp")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoUngrp(EnumAttribute):
    """Запрет разгруппировки"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noUngrp")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoDrilldown(EnumAttribute):
    """Запрет детализации (SmartArt)"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noDrilldown")

    class Options(Enum):
        access = "0"
        restrict = "1"


class NoTextEdit(EnumAttribute):
    """Запрет редактирования текста"""

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="noTextEdit")

    class Options(Enum):
        access = "0"
        restrict = "1"
