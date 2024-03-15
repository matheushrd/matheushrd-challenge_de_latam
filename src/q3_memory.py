from memory_profiler import profile
from typing import List, Tuple
from datetime import datetime
from questions import DataAnalyzer
import logging

logging.basicConfig(level=logging.INFO)


@profile
def q3_memory(analyzer: DataAnalyzer) -> List[Tuple[str, int]]:
    # Create an instance of DataAnalyzeR
    return analyzer.q3()

# if __name__ == '__main__':
#     logging.info(q3_memory())

