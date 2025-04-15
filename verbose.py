
from VerbositySettings import VERBOSITY_LEVEL

LEVELS = {
    "CRITICAL": 0,
    "INFO": 1,
    "DEBUG": 2
}

def log(msg, level="INFO"):
    if LEVELS[level] <= LEVELS.get(VERBOSITY_LEVEL, 1):
        print(msg, flush=True)
