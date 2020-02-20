# This is a sample macro file with a single command.  When NatSpeak has the
# focus, say "demo natlink".  It should recognize the command and print it.

import natlink
from natlinkutils import *

class ThisGrammar(GrammarBase):

    gramSpec = """
        <start> exported = demo natlink;
    """
    
    def initialize(self):
        self.load(self.gramSpec)
        self.activateAll()

    def gotResults_start(self,words,fullResults):
		print 'Detected "demo natlink"'

thisGrammar = ThisGrammar()
thisGrammar.initialize()

print 'Demo Natlink command loaded, say "demo natlink"!'

def unload():
    global thisGrammar
    if thisGrammar: thisGrammar.unload()
    thisGrammar = None
