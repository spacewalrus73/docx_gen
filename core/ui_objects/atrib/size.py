from core.ui_objects.base.base_attribute import SimpleAttribute

# """Размеры в EMU (English Metric Units)"""

class Height(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="w:h")


class Width(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="w:w")


class CX(SimpleAttribute):

    def __init__(self, value: int):

        super().__init__(value=value, xml_name="cx")


class CY(SimpleAttribute):

    def __init__(self, value: int):
        super().__init__(value=value, xml_name="cy")


class EffectLeft(SimpleAttribute):

    def __init__(self, value: int):
        super().__init__(value=value, xml_name="l")


class EffectTop(SimpleAttribute):

    def __init__(self, value: int):
        super().__init__(value=value, xml_name="t")


class EffectRight(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="r")


class EffectBottom(SimpleAttribute):
    def __init__(self, value: int):
        super().__init__(value=value, xml_name="b")
