from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum

class ObjectId(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="id")


class ObjectName(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="name")


class ObjectDescr(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="descr")


class ObjectTitle(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="title")


class ObjectHidden(EnumAttribute):

    def __init__(self, value: str):
        super().__init__(value=value, xml_name="hidden")

    class Options(Enum):
        hidden = "1"
        visible = "0"
