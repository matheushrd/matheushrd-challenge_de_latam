from typing import List, Tuple
import cProfile
from questions import DataAnalyzer
import logging
import pstats

logging.basicConfig(level=logging.INFO)


def q3_time(analyzer: DataAnalyzer) -> List[Tuple[str, int]]:
    return analyzer.q3()


def q3_run_profiler(analyzer: DataAnalyzer):
    cProfile.run("q3_time(analyzer)", "q3_stats")
    p = pstats.Stats("q3_stats")
    p.sort_stats("time").print_stats(20)