"""
    Subset Sum Functions
"""
import time

TIME_LIMIT = 2 # seconds

class SummerRuntimeError(RuntimeError): pass
class SummerTimeoutError(SummerRuntimeError): pass

def diophantine_subset_sum(number_list, target, time_limit=TIME_LIMIT):
    """Takes a positive list of integers along with a target and returns a subset of
    numbers from list matching target. Implements diophantine linear algorithm described here:

    https://web.archive.org/web/20091018234158/http://geocities.com/SiliconValley/Garage/3323/aat/a_diop.html
    """
    started_at = time.time()

    # Sort numbers list.
    number_list = sorted(number_list)

    # Build sums list.
    sums_list = [number_list[0]]
    for n in range(1, len(number_list)):
        sums_list.append(number_list[n] + sums_list[n-1])

    # Sanity check target.
    if number_list[0] > target or target > sums_list[-1]:
        return []

    # Add first subset to subset stack.
    subset_stack = [(len(number_list)-1, target, ())]

    # Process subset stack.
    while subset_stack:
        # Enforce time constraint.
        runtime = time.time() - started_at
        if runtime > time_limit:
            raise SummerTimeoutError('No solution found in %d seconds.' % (time_limit))

        # Pop first subset off queue
        offset, subtarget, subset = subset_stack.pop()

        # Keeps only sums less than subset target.
        sumlist_offset = 0
        while sums_list[sumlist_offset] < subtarget and sumlist_offset < len(sums_list)-1:
          sumlist_offset += 1

        # If next sums list value matches subset target, we have a solution.
        if sums_list[sumlist_offset] == subtarget:
            return subset + tuple(number_list[0:sumlist_offset+1])

        # Keep only numbers in list less than subset target.
        while number_list[offset] > subtarget and offset > 0:
            offset = offset - 1

        # If next number in list matches subset target, we have a solution.
        if number_list[offset] == subtarget:
            return subset + tuple([number_list[offset]])

        # Add subsets to queue for any number list values falling between sums list
        # offset and numbers list offset
        step = (sumlist_offset <= offset) and 1 or -1
        for new_offset in range(sumlist_offset, offset+step, step):

            new_subset = subset + tuple([number_list[new_offset]])
            new_subtarget = subtarget - number_list[new_offset]

            if number_list[0] > new_subtarget:
                break

            subset_stack.append((new_offset-1, new_subtarget, new_subset))

    # Solution not found
    return []
