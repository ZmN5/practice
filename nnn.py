def threeSum(nums):
    """
    :type nums: List[int]
    :rtype: List[List[int]]
    """
    l = len(nums)
    if l < 3:
        return []
    res = []
    nums.sort()
    start = 0;
    end = l - 1
    flag = 0
    while start < end - 1:
        tmp = nums[start] + nums[end]
        target = 0 - tmp
        mid = (start + end) // 2
        tstart = start;
        tend = end
        while tstart < mid < tend and nums[tstart] <= target <= nums[tend]:
            if nums[mid] == target:
                flag = 1
                res.append([nums[start], nums[mid], nums[end]])
                break
            elif nums[mid] > target:
                t = mid
                mid = (tstart + mid) // 2
                tend = t
            else:
                t = mid
                mid = (mid + tend) // 2
                tstart = t
        if flag == 1:
            flag = 0
            subnums = nums[start:end]
            res.append(threeSum(subnums))
            subnums = nums[start + 1:end+1]
            res.append(threeSum(subnums))
            t = start
            while start < end and nums[t] == nums[start]:
                start += 1
            t = end
            while start < end and nums[t] == nums[end]:
                end -= 1
        else:
            if tmp < 0:
                start += 1
            else:
                end -= 1
    return res

if __name__ == '__main__':
    res=threeSum([-2,0,1,1,2])
    print(res)