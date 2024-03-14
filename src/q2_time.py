from typing import List, Tuple
from datetime import datetime
import cProfile
from questions import DataAnalyzer
import logging
import pstats

logging.basicConfig(level=logging.INFO)

analyzer = DataAnalyzer()
def q2_time() -> List[Tuple[str, int]]:
    # Call the q1 method on the instance
    return analyzer.q2()

cProfile.run("q2_time()", "q2_stats")
p = pstats.Stats("q2_stats")
p.sort_stats("time").print_stats(20)