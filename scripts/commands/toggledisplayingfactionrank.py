from resources.common import PlayerFlags
import sys

def setup():
    return
    
def run(core, actor, target, commandString):
    ghost = actor.getSlottedObject('ghost')
    ghost.toggleFlag(PlayerFlags.FACTIONRANK)
    return