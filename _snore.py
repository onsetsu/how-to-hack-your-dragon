# gracefully stolen from https://github.com/simianhacker/code-by-voice/blob/master/macros/_snore.py

from dragonfly import *
import natlink

config = Config("snore");
config.lang = Section("Language section");
config.lang.snore = Item("snore", doc="Put the microphone to sleep")


class SnoreRule(CompoundRule):
    spec = config.lang.snore

    def _process_recognition(self, node, extras):
        self._log.debug("sleepy mic")
        natlink.setMicState("sleeping")

grammar = Grammar("snore")
grammar.add_rule(SnoreRule())
grammar.load()


def unload():
    global grammar
    if grammar: grammar.unload()
    grammar = None
