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
        "Hans Wurst": Text("WOOOOOOOW"),
		"aether": Text("aexpr(() => )") + Key("left"),
		"open debugger": Key("cs-j"),
		"open workspace": Key("c-k"),
		"open sync tool": Key("cs-g"),
        },
    extras=[
        IntegerRef("n", 1, 100),
        Dictation("text"),
        ],
    defaults={
        "n": 1
    }
)

grammar = Grammar("Programming help", context=None)
grammar.add_rule(demo_rule)
grammar.load()
# foobarbarbarfoobarfoobar
##foo
#foofoobar
# Unload function which will be called at unload time.
def unload():
    global grammar
    if grammar:
        grammar.unload()
    grammar = None