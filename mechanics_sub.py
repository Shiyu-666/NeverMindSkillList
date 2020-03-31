from mechanics import Mechanic


class ActivateSpawner(Mechanic):
    def __init__(self):
        Mechanic.__init__(self)
        self.attrs = [
            [('spawners', 'The name of the spawner(s) to activate. This can accept groups and wildcards also using the appropriate syntax', 'NONE'), 'NONE'],
        ]
        self.desc = 'Activates a MythicMobs spawner, causing it to spawn mobs. Will not override any conditions or options set on the spawner.'
        self.comment = ''
        self.kind = 'mechanic'


class ArrowVolley(Mechanic):
    def __init__(self):
        Mechanic.__init__(self)
        self.attrs = [
            [('amount', 'The number of arrows in the volley', '20'), '20'],
            [('spread', 'How spread out the arrows are', '45'), '45'],
            [('velocity', 'The velocity of the arrows', '20'), '20'],
            [('fireTicks', 'The duration hit entities will burn for in ticks', '0'), '0'],
            [('removeDelay', 'The time the arrows will stay before disappearing in ticks', '200'), '200'],
        ]
        self.desc = 'Fires a volley of arrows towards the target with a number of configurable properties.'
        self.comment = ''
        self.kind = 'mechanic'


class BarCreate(Mechanic):
    def __init__(self):
        Mechanic.__init__(self)
        self.attrs = [
            [('name', 'The name of the bossbar.', 'infobar'), 'infobar'],
            [('display', 'The text displayed on the bar.', '<skill.var.aura-name>'), '<skill.var.aura-name>'],
            [('value', 'How filled the bossbar is. Must be between 0.0 and 1.0.', '1.0'), '1.0'],
            [('color', 'The color of the bossbar. Accepts the following: PINK, BLUE, RED, GREEN, YELLOW, PURPLE, WHITE.', 'RED'), 'RED'],
            [('style', 'The style of the bossbar. Accepts the following: SOLID, SEGMENTED_6, SEGMENTED_10, SEGMENTED_12, SEGMENTED_20 .', 'SOLID'), 'SOLID'],
        ]
        self.desc = 'Creates a custom boss bar on the casting mob.'
        self.comment = ''
        self.kind = 'mechanic'


class BarSet(Mechanic):
    def __init__(self):
        Mechanic.__init__(self)
        self.attrs = [
            [('name', 'The name of the bossbar.', 'infobar'), 'infobar'],
            [('display', 'The text displayed on the bar.', '<skill.var.aura-name>'), '<skill.var.aura-name>'],
            [('value', 'How filled the bossbar is. Must be between 0.0 and 1.0.', '1.0'), '1.0'],
        ]
        self.desc = 'Modifies a custom boss bar on the casting mob.'
        self.comment = ''
        self.kind = 'mechanic'


class BarRemove(Mechanic):
    def __init__(self):
        Mechanic.__init__(self)
        self.attrs = [
            [('name', 'The name of the bossbar.', 'infobar'), 'infobar'],
        ]
        self.desc = 'Removes a custom boss bar on the casting mob.'
        self.comment = ''
        self.kind = 'mechanic'


class Command(Mechanic):
    def __init__(self):
        Mechanic.__init__(self)
        self.attrs = [
            [('command', 'The command to execute', ''), ''],
            [('asCaster', 'If true the command will execute from the caster instead of the console.', 'false'), 'false'],
            [('asOp', 'Whether to execute the command with all permissions', 'false'), 'false'],
        ]
        self.desc = 'Executes a command for each target supplied.'
        self.comment = ''
        self.kind = 'mechanic'


