from core.ui_objects.base.base_attribute import SimpleAttribute


class Top(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:top")


class Left(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:left")


class Right(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:right")


class Bottom(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:bottom")


class Space(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:space")


class LinePitch(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="w:linePitch")


class DistTop(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:distT")


class DistLeft(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:distL")


class DistRight(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:distR")


class DistBottom(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="wp:distB")
