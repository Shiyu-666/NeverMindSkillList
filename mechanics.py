class Mechanic:
    def __init__(self):
        self.targeter = ''
        self.uattrs = [
            [('cooldown', 'cd', 'In seconds', '0', 'int'), '0'],
            [('delay', '', 'Delays the execution of the mechanic', '0', 'int'), '0'],
            [('repeat', '', 'How many times the mechanic should be repeated', '0', 'int'), '0'],
            [('repeatInterval', '', 'How many ticks must elapse between repetitions', '0', 'int'), '0']
        ]
