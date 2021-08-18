from constants import *


def getPieceImage(identification):
    if identification == 'o':
        return ORANGEP
    elif identification == 'b':
        return BROWNP
    elif identification == 'oq':
        return ORANGEQ
    elif identification == 'bq':
        return BROWNQ
    return None


def getPieceIsBlank(identification):
    if identification == 'n':
        return True
    return False


def getPieceIsHuman(identification):
    if identification == 'o' or identification == 'oq':
        return True
    return False