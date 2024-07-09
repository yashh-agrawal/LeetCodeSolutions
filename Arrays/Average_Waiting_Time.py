# There is a restaurant with a single chef. You are given an array customers, where customers[i] = [arrivali, timei]:

# arrivali is the arrival time of the ith customer. The arrival times are sorted in non-decreasing order.
# timei is the time needed to prepare the order of the ith customer.
# When a customer arrives, he gives the chef his order, and the chef starts preparing it once he is idle. 
# The customer waits till the chef finishes preparing his order. The chef does not prepare food for more than one customer at a time.
# The chef prepares food for customers in the order they were given in the input.

# Return the average waiting time of all customers. Solutions within 10-5 from the actual answer are considered accepted.

class Solution:
    def averageWaitingTime(self, customers: List[List[int]]) -> float:
        wait_time = customers[0][1]
        prev_finish = customers[0][0] + customers[0][1]
        n = len(customers)
        for i in range(1, n, 1):
            times = customers[i]
            arrives = times[0]

            start_cook = max(arrives, prev_finish)
            end_time = start_cook + times[1]
            prev_finish = end_time
            wait_time += end_time - arrives
        
        return wait_time / n