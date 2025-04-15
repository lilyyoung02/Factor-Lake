class VerbosityManager:
    LEVELS = {
        'CRITICAL': 0,
        'INFO': 1,
        'DEBUG': 2
    }

    def __init__(self, level='INFO'):
        self.level = self.LEVELS.get(level.upper(), 1)

    def set_level(self, level):
        self.level = self.LEVELS.get(level.upper(), 1)

    def critical(self, message):
        if self.level >= self.LEVELS['CRITICAL']:
            print(message)

    def info(self, message):
        if self.level >= self.LEVELS['INFO']:
            print(message)

    def debug(self, message):
        if self.level >= self.LEVELS['DEBUG']:
            print(message)
