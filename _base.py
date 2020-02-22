from dragonfly import (
    CompoundRule,
    MappingRule,
    RuleRef,
    Repetition,
    Dictation,
    IntegerRef,
    Grammar,
    Key,
    Text,

)

base_rule = MappingRule(
    mapping={
        "safe": Key("c-s"),
        "reload": Key("home/10, home"),
        "update": Key("c-s/30, home/10, home"),
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
    ],
    defaults={
        "n": 1
    }
)

grammar = Grammar("Basic Commands", context=None)
grammar.add_rule(base_rule)
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None
