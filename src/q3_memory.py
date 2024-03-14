from memory_profiler import profile
from typing import List, Tuple
from datetime import datetime
from questions import DataAnalyzer  # Assuming DataAnalyzer is in DataAnalyzer.py

@profile
def q3_memory() -> List[Tuple[str, int]]:
    # Create an instance of DataAnalyzer
    analyzer = DataAnalyzer()

    # Call the q3 method on the instance
    return analyzer.q3()

if __name__ == '__main__':
    q3_memory()
