from typing import List, Tuple
import cProfile
from questions import DataAnalyzer
import logging
import pstats

logging.basicConfig(level=logging.INFO)


def q2_time(analyzer: DataAnalyzer) -> List[Tuple[str, int]]:
    return analyzer.q2()


def q2_run_profiler(analyzer: DataAnalyzer):
    cProfile.run("q2_time(analyzer)", "q2_stats")
    p = pstats.Stats("q2_stats")
    p.sort_stats("time").print_stats(20)