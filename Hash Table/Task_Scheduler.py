# You are given an array of CPU tasks, each labeled with a letter from A to Z, and a number n. Each CPU interval can be idle or allow the completion of one task. Tasks can be completed in any order, but there's a constraint: there has to be a gap of at least n intervals between two tasks with the same label.

# Return the minimum number of CPU intervals required to complete all tasks.

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        freq = Counter(tasks)

        freq = sorted(freq.values(), reverse=True)
        max_freq = freq[0]

        idle_time = (max_freq - 1) * n

        for freq in freq[1:]:
            idle_time -= min(max_freq - 1, freq)
        
        idle_time = max(0, idle_time)

        return len(tasks) + idle_time