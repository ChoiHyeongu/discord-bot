from enum import Enum

# 명령어
class Command(Enum):
    # Game
    RPS = '~RPS'
    LADDER = '~ladder'
    BOMB = '~bomb'
    WORD_CHAIN = '~wordchain'
    TITACTOE = '~ttt'
    NUMBER_BASEBALL = '~numbaseball'

    # Project
    DEADLINE = "~deadline"

    # Picture
    OROGI = '~orogi'

    # Aggro
    AGGRO = '애들아 나 할말 있어...'

    # Test
    TEST = '~test'