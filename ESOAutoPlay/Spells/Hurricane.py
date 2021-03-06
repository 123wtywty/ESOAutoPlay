from Spells.Spell import Spell, CurrentStates
import time


class Hurricane(Spell):
    spellName = "Hurricane"

    spellBar = 1
    spellSlot = 4

    priority = 7

    nextTimeUseIt = 0
    duration = 15

    def __init__(self, priority=7):
        Spell.__init__(self)
        self.priority = priority

    def shouldUseThisSpell(self, states: CurrentStates):
        Spell.currentStates = states
        if self.nextTimeUseIt < time.time() and states.haveEnoughMagicka:
            return True
        else:
            return False

    def use(self):
        self.nextTimeUseIt = time.time() + self.duration
        super().use()

