from memory_profiler import profile
from typing import List, Tuple
from datetime import datetime
from questions import DataAnalyzer
import logging

logging.basicConfig(level=logging.INFO)


@profile
def q2_memory(analyzer: DataAnalyzer) -> List[Tuple[str, int]]:
    return analyzer.q3()
