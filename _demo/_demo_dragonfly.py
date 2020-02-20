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

demo_rule = MappingRule(
    mapping={
        "foo [<n>]": Key("f, o:%(n)d"),
    },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
        ],
    defaults={
        "n": 2
    }
)

grammar = Grammar("Programming help", context=None)
grammar.add_rule(demo_rule)
grammar.load()

def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None