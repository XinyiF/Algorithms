def BinarySearch(sortedArr,target,HigherBound=False):
    """

    :param sortedArr:
    :param target:
    :param HigherBound:
    :return:
    """
    low,high=0,len(sortedArr)-1
    # 为了确认上下边界
    # low high 会在最后选择时重合
    while low <= high:
        if HigherBound:
            if sortedArr[high] == target:
                return high
            # 找上边界要向上取整
            mid = low + (high - low+1) // 2
            # low快速收缩
            if sortedArr[mid] < target:
                low = mid + 1
            elif sortedArr[mid] > target:
                high=mid-1
            else:
                low=mid
        else:
            if sortedArr[low] == target:
                return low
            mid = low + (high - low) // 2
            if sortedArr[mid] > target:
                high = mid-1
            elif sortedArr[mid] < target:
                low = mid+1
            else:
                high=mid
    return -1


list=[5,7,7,8,8,10]
print(BinarySearch(list,8,True))