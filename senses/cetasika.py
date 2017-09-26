# Cetasika


from enum import IntEnum


class CetasikaType(IntEnum):
    # 52 types of cetasika
    # universals - ethically variable
    Contact = 0
    Feeling = 1
    Perception = 2
    Volition = 3
    One_pointedness = 4
    Life_faculty = 5
    Attention = 6
    # these are occationals
    Init_application = 7
    Sustained_application = 8
    Decision = 9
    Energy = 10
    Zest = 11
    Desire = 12
    # unwholesome universals
    Delusion = 13
    Shamelessness = 14
    Fearlessness_of_wrong = 15
    Restlessness = 16
    # unwholesome occationals
    Greed =  17
    Wrong_view = 18
    Conceit = 19
    Hatred = 20
    Envy = 21
    Avarice = 22
    Worry = 23
    Sloth = 24
    Torpor = 25
    Doubt = 26
    # Beautiful universals
    Faith = 27
    Mindfulness = 28
    Shame = 29
    Fear_of_wrong = 30
    Nongreed = 31
    Nonhatred = 32
    Neutrality_mind = 33
    Tranquility_mental_body = 34
    Tranquility_consciousness = 35
    Lightness_mental_body = 36
    Lightness_consciousness = 37
    Malleability_mental_body = 38
    Malleability_consciousness = 39
    Wieldiness_mental_body = 40
    Wieldiness_consciousness = 41
    Proficiency_mental_body = 42
    Proficiency_consciousness = 43
    Rectitude_mental_body = 44
    Rectitude_consciousness = 45
    # Abstinences
    Right_speech = 46
    Right_action = 47
    Right_livelihood = 48
    # Illimitables
    Compassion = 49
    Appreciative_joy = 50
    # Non-delusion
    Wisdom_faculty = 51

    def wholesomeness(self, i_ce):
        if i_ce > 26:
            return 1
        elif i_ce < 13:
            return 0  # variable or unknown
        else:
            return -1


class CetasikaBase(object):
    # each Cetasika keeps a dictionary of attributes or values
    # e.g. Feeling has pleasant, unpleasant and neutral; wisdom can have scale
    # for now, unless we know specifics, we treat them as binary
    def __init__(self, citta):
        self.citta = citta

