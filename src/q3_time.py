from typing import List, Tuple
from datetime import datetime
import cProfile
from questions import DataAnalyzer
import logging
import pstats

logging.basicConfig(level=logging.INFO)

analyzer = DataAnalyzer()

def q3_time() -> List[Tuple[str, int]]:
    # Call the q3 method on the instance
    return analyzer.q3()

cProfile.run("q3_time()", "q3_stats")
p = pstats.Stats("q3_stats")
p.sort_stats("time").print_stats(20)