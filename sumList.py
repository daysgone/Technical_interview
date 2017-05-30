nums: [3, 0, -2, 6, -3, 2]
queries: [[0,2],
 [2,5],
 [0,5]

def sumInRange(nums, queries):
    sumlist = []
    for query in queries:
        sum = 0
        for index in query:
            sum += nums[index]
        sumlist.append(sum)
        return sumlist

print sumInRange()