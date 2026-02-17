from core.ui_objects.base.base_attribute import TwipsAttribute
from core.utils.metrics import Length


class Height(TwipsAttribute):
    def __init__(self, value: Length):
        super().__init__(value=value, xml_name="w:h")


class Width(TwipsAttribute):
    def __init__(self, value: Length):
        super().__init__(value=value, xml_name="w:w")
