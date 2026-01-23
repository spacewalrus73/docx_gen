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
