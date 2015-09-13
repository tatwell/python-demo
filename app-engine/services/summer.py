"""
    Subset Sum Functions
"""
from collections import deque
import time

DEFAULT_PRECISION = .00001
CYCLE_LIMIT = 1000000
TIME_LIMIT = 2 # seconds
DEBUG = False

class SubsetRuntimeError(RuntimeError): pass
class TimeoutError(SubsetRuntimeError): pass
class MaximumCycleError(SubsetRuntimeError): pass

def debug(*message):
    if DEBUG:
        print '[DEBUG] %s' % (' '.join(message))


def diophantine_subset_sum(number_list, target):
    # DIOPHANT: procedure expose A.
    # parse arg N, T
    cycles = 0
    started_at = time.time()

    # call QUICKSORT N
    number_list = sorted(number_list)

    # Ls.1 = A.1
    # do I = 2 to N
    #   Im1 = I - 1; Ls.I = A.I + Ls.Im1
    # end
    sums_list = [number_list[0]]
    for n in range(1, len(number_list)):
        sums_list.append(number_list[n] + sums_list[n-1])

    # if A.1 <= T & T <= Ls.N then do
    if number_list[0] > target or target > sums_list[-1]:
        return []

    # S = 1; Stack.1 = N T
    subset_queue = deque()
    subset_queue.append((len(number_list)-1, target, ()))

    # do while S > 0
    while subset_queue:
        #print cycles
        cycles += 1
        if cycles > CYCLE_LIMIT:
            raise MaximumCycleError('Exceed cycle limit: %s' % (CYCLE_LIMIT))

        runtime = time.time() - started_at
        if runtime > TIME_LIMIT:
            raise TimeoutError(runtime)

        # parse var Stack.S R T V; S = S - 1
        offset, subtarget, subset = subset_queue.popleft()

        # do K = 1 while Ls.K < T; end
        # Keeps only sums less than target
        sumlist_offset = 0
        while sums_list[sumlist_offset] < subtarget:
          sumlist_offset += 1

        # if Ls.K = T then call EXIST V, K, 1
        if sums_list[sumlist_offset] == subtarget:
            debug('Ls.K = T')
            return subset + tuple(number_list[0:sumlist_offset+1])

        # do while A.R > T; R = R - 1; end
        # Keep only numbers in list less than target
        while number_list[offset] > subtarget and offset > 0:
            offset = offset - 1

        # if A.R = T then call EXIST V, R, R
        if number_list[offset] == subtarget:
            debug('A.R = T')
            return subset + tuple([number_list[offset]])

        # do L = K to R while A.1 <= T - A.L
        # Add to stack subsets within target parameters
        step_start = min(sumlist_offset, offset)
        step_end = max(sumlist_offset, offset) + 1
        debug('step start-end', step_start, step_end)
        numbers_within_target = True
        for new_offset in range(step_start, step_end):

            # D = V A.L; S = S + 1
            new_subset = subset + tuple([number_list[new_offset]])
            new_subtarget = subtarget - number_list[new_offset]

            if number_list[0] > new_subtarget:
                break

            # Stack.S = (L - 1) (T - A.L) D
            subset_queue.append((new_offset-1, new_subtarget, new_subset))

    #say "Solution not exist"
    return []
