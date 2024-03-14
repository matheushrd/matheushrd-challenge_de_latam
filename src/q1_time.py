from typing import List, Tuple
from datetime import datetime
import cProfile
from questions import DataAnalyzer
import logging
import pstats

logging.basicConfig(level=logging.INFO)

analyzer = DataAnalyzer()

def q1_time() -> List[Tuple[datetime.date, str]]:
    # Call the q1 method on the instance
    return analyzer.q1()

cProfile.run("q1_time()", "q1_stats")
p = pstats.Stats("q1_stats")
p.sort_stats("time").print_stats(20)