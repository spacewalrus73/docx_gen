from core.ui_objects.base.base_attribute import TwipsAttribute
from core.utils.metrics import Twips


class Top(TwipsAttribute):
    def __init__(self, value: Twips):
        super().__init__(value=value, xml_name="w:top")


class Left(TwipsAttribute):
    def __init__(self, value: Twips):
        super().__init__(value=value, xml_name="w:left")


class Right(TwipsAttribute):
    def __init__(self, value: Twips):
        super().__init__(value=value, xml_name="w:right")


class Bottom(TwipsAttribute):
    def __init__(self, value: Twips):
        super().__init__(value=value, xml_name="w:bottom")


class Space(TwipsAttribute):
    def __init__(self, value: Twips):
        super().__init__(value=value, xml_name="w:space")


class LinePitch(TwipsAttribute):
    def __init__(self, value: Twips):
        super().__init__(value=value, xml_name="w:linePitch")
