from memory_profiler import profile
from typing import List, Tuple
from datetime import datetime
from questions import DataAnalyzer
import logging

logging.basicConfig(level=logging.INFO)


@profile
def q1_memory(analyzer: DataAnalyzer) -> List[Tuple[datetime.date, str]]:
    return analyzer.q1()
