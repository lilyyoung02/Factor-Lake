import sys
import os

#adding the project root directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import cProfile
import pstats
from pstats import SortKey
from main import main

cProfile.run('main()', 'main_stats')
p = pstats.Stats('main_stats')
p.sort_stats(SortKey.CUMULATIVE).print_stats(10)