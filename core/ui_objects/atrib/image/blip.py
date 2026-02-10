from core.ui_objects.base.base_attribute import SimpleAttribute, EnumAttribute
from enum import Enum


# ========== ПРОЗРАЧНОСТЬ ==========


class Embed(SimpleAttribute):
    def __init__(self, value: str):
        super().__init__(value=value, xml_name="r:embed")


class CState(EnumAttribute):
    """Состояние сжатия изображения"""

    def __init__(self, value: str = "print"):
        super().__init__(value=value, xml_name="cstate")

    class Options(Enum):
        print = "print"
        screen = "screen"
        hq = "hq"
        always = "always"


class AlphaMod(SimpleAttribute):
    """Модификатор прозрачности (0-100000)"""

    def __init__(self, value: str = "10000"):
        super().__init__(value=value, xml_name="alphaMod")


class AlphaModFix(SimpleAttribute):
    """Фиксированный модификатор прозрачности (0-100000)"""

    def __init__(self, value: str = None):
        super().__init__(value=value, xml_name="alphaModFix")


# ========== ЯРКОСТЬ И КОНТРАСТ ==========

class Gain(SimpleAttribute):
    """Усиление яркости (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="gain")


class BlackLevel(SimpleAttribute):
    """Уровень черного (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="blackLevel")

    def validate(self, value: str):
        val = int(value)
        if not 0 <= val <= 100000:
            raise ValueError(f"blackLevel должен быть от 0 до 100000, получено: {val}")


class Gamma(SimpleAttribute):
    """Гамма-коррекция (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="gamma")


# ========== ОСНОВНЫЕ ЦВЕТА ==========


class Gray(SimpleAttribute):
    """Коррекция серого канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="gray")


class Red(SimpleAttribute):
    """Коррекция красного канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="red")


class Green(SimpleAttribute):
    """Коррекция зеленого канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="green")


class Blue(SimpleAttribute):
    """Коррекция синего канала (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="blue")


# ========== МОДИФИКАТОРЫ ЦВЕТОВ ==========

class RedMod(SimpleAttribute):
    """Модификатор красного канала (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="redMod")


class GreenMod(SimpleAttribute):
    """Модификатор зеленого канала (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="greenMod")


class BlueMod(SimpleAttribute):
    """Модификатор синего канала (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="blueMod")


# ========== HSL (HUE, SATURATION, LUMINANCE) ==========

class Hue(SimpleAttribute):
    """Оттенок (0-21600000, где 21600000 = 360°)"""

    def __init__(self, value: str = "10000"):
        super().__init__(value=value, xml_name="hue")


class HueMod(SimpleAttribute):
    """Модификатор оттенка (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="hueMod")


class Sat(SimpleAttribute):
    """Насыщенность (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="sat")


class SatMod(SimpleAttribute):
    """Модификатор насыщенности (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="satMod")


class Lum(SimpleAttribute):
    """Яркость (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="lum")


class LumMod(SimpleAttribute):
    """Модификатор яркости (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="lumMod")


# ========== КОНТРАСТ И РЕЗКОСТЬ ==========

class Cont(SimpleAttribute):
    """Контрастность (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="cont")


class ContMod(SimpleAttribute):
    """Модификатор контрастности (0-100000)"""

    def __init__(self, value: str = "100000"):
        super().__init__(value=value, xml_name="contMod")


class Sharp(SimpleAttribute):
    """Резкость (-100000..100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="sharp")


# ========== ДРУГИЕ ЭФФЕКТЫ ==========

class Shade(SimpleAttribute):
    """Затемнение (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="shade")


class Tint(SimpleAttribute):
    """Тонирование (0-100000)"""

    def __init__(self, value: str = "0"):
        super().__init__(value=value, xml_name="tint")


# ========== ЦВЕТА ЗАЛИВКИ ==========

class BuClr(SimpleAttribute):
    """Цвет фона (background color) в формате RRGGBB hex"""

    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="buClr")


class BuClrTx(SimpleAttribute):
    """Цвет текста фона (background color text) в формате RRGGBB hex"""

    def __init__(self, value: str = ""):
        super().__init__(value=value, xml_name="buClrTx")
