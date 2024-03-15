from typing import List, Tuple
from datetime import datetime
import cProfile
from questions import DataAnalyzer
import logging
import pstats

logging.basicConfig(level=logging.INFO)


def q1_time(analyzer: DataAnalyzer) -> List[Tuple[datetime.date, str]]:
    # Call the q1 method on the instance
    return analyzer.q1()


def q1_run_profiler(analyzer: DataAnalyzer):
    cProfile.run("q1_time(analyzer)", "q1_stats")
    p = pstats.Stats("q1_stats")
    p.sort_stats("time").print_stats(20)