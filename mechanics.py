class Mechanic():

    def __init__(self):
        self.uattrs = {
            'cooldown': [('cooldown', 'cd', 'In seconds', '0', 'int'), '0'],
            'delay': [('delay', '', 'Delays the execution of the mechanic', '0', 'int'), '0'],
            'repeat': [('repeat', '', 'How many times the mechanic should be repeated', '0', 'int'), '0'],
            'repeatInterval': [('repeatInterval', '', 'How many ticks must elapse between repetitions', '0', 'int'), '0']
        }


class ActivateSpawner(Mechanic):

    def __init__(self):

        self.attrs = {
            'spawners': [('spawners', 's', 'The name of the spawner(s) to activate. This can accept groups and wildcards also using the appropriate syntax', '', 'str'), '']
        }
