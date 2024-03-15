from memory_profiler import profile
from typing import List, Tuple
from datetime import datetime
from questions import DataAnalyzer  # Assuming DataAnalyzer is in DataAnalyzer.py
import logging

logging.basicConfig(level=logging.INFO)


@profile
def q2_memory(analyzer: DataAnalyzer) -> List[Tuple[str, int]]:
    # Create an instance of DataAnalyzer
    return analyzer.q3()

# if __name__ == '__main__':
#     logging.info(q2_memory(analyzer))
