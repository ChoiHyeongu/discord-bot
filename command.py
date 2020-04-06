from enum import Enum

class Command(Enum):
    # Game
    RPS = '~RPS'
    LADDER = '~ladder'
    BOMB = '~bomb'
    WORD_CHAIN = '~wordchain'
    TITACTOE = '~ttt'
    NUMBER_BASEBALL = '~numbaseball'

    #Picture
    OROGI = '~orogi'

    #Aggro
    AGGRO = '~aggro'