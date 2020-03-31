class Mechanic:
    def __init__(self):
        self.targeter = ''
        self.uattrs = [
            [('cooldown', 'In seconds', '0'), '0'],
            [('delay', 'Delays the execution of the mechanic', '0'), '0'],
            [('repeat', 'How many times the mechanic should be repeated', '0'), '0'],
            [('repeatInterval', 'How many ticks must elapse between repetitions', '0'), '0']
        ]
