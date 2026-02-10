from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum


class ImageHidden(EnumAttribute):

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="hidden")

    class Options(Enum):
        hidden = "1"
        visible = "0"


class ImageId(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="id")


class ImageName(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="name")


class ImageDescr(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="descr")


class ImageTitle(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="title")



class URIGraphicData(EnumAttribute):
    class Options(Enum):
        pic = "http://schemas.openxmlformats.org/drawingml/2006/picture"
        chart = "http://schemas.openxmlformats.org/drawingml/2006/chart"
        diagram = "http://schemas.openxmlformats.org/drawingml/2006/diagram"
        smartart = "http://schemas.microsoft.com/office/drawing/2010/main"
        drawing = "http://schemas.openxmlformats.org/drawingml/2006/wordprocessingDrawing"
        model = "http://schemas.microsoft.com/office/drawing/2017/model3d"
        ink = "http://schemas.microsoft.com/office/drawing/2016/ink"

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="uri")


class URIExt(SimpleAttribute):
    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="uri")

class Dpi(SimpleAttribute):
    """DPI для fillRect (0 = использовать системный DPI)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="dpi")


class UseLocalDpiVal(EnumAttribute):
    """Значение для useLocalDpi"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="val")

    class Options(Enum):
        use_system = "0"  # Использовать системный DPI
        use_local = "1"  # Использовать локальный DPI из файла