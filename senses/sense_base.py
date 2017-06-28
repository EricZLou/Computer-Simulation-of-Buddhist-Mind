# Sense base object

class SenseBase(object):
    def __init__(self, strength):
        self.strength = strength


class SenseEye(SenseBase):
    # vision [left right] strength
    def __init__(self, vision):
        super().__init__(min(vision[0], vision[1]))
        self.vision = vision


class SenseEar(SenseBase):
    # hearing [left right] strength
    def __init__(self, hearing):
        super().__init__(min(hearing[0], hearing[1]))
        self.hearing = hearing


class SenseNose(SenseBase):
    # smell strength
    def __init__(self, nosesens):
        super().__init__(nosesens)
        self.nosesens = nosesens


class SenseTongue(SenseBase):
    # taste strength
    def __init__(self, tonguesens):
        super().__init__(tonguesens)
        self.tonguesens = tonguesens


class SenseBody(SenseBase):
    # taste strength
    def __init__(self, bodysens):
        super().__init__(bodysens)
        self.bodysens = bodysens

