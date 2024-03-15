from q1_memory import q1_memory
from q2_memory import q2_memory
from q3_memory import q3_memory

from q1_time import q1_run_profiler, q1_time
from q2_time import q2_run_profiler, q2_time
from q3_time import q3_run_profiler, q3_time

from questions import DataAnalyzer

if __name__ == '__main__':
    analyzer = DataAnalyzer()
    
    q1_memory(analyzer= analyzer)
    q3_memory(analyzer= analyzer)
    q2_memory(analyzer= analyzer)

    q1_run_profiler(analyzer= analyzer)
    q2_run_profiler(analyzer= analyzer)
    q3_run_profiler(analyzer= analyzer)
    
    