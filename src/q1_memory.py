from memory_profiler import profile
from typing import List, Tuple
from datetime import datetime
from questions import DataAnalyzer  # Assuming DataAnalyzer is in DataAnalyzer.py
import logging

logging.basicConfig(level=logging.INFO)


@profile
def q1_memory() -> List[Tuple[datetime.date, str]]:
    # Create an instance of DataAnalyzer
    analyzer = DataAnalyzer()

    # Call the q1 method on the instance
    return analyzer.q1()

if __name__ == '__main__':
    logging.info(q1_memory())
