# 二分查找问题
# l=0 r=N-1
# while l<=r
# 如果找插入位置 leftbinsearch
# leftbinsearch 在相等的时候 缩小r 最后返回l
# rightbinsearch 在相等的时候 缩小l 最后返回r


def binsearch(nums,target):
    n = len(nums)
    l,r = 0, n-1
    while l<=r:
        mid = (l+r)//2
        if nums[mid]==target:
            return mid
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1

def leftbinsearch(nums, target):
    N = len(nums)
    l,r=0,N-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]==target:
            r=mid-1
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return l



nums=[1,2,4,4,4,4,4,5,6]
def rightbinsearch(nums, target):
    N = len(nums)
    l,r=0,N-1
    while l<=r:
        mid=l+(r-l)//2
        if nums[mid]==target:
            l=mid+1
        elif nums[mid]<target:
            l=mid+1
        else:
            r=mid-1
    return r

print(leftbinsearch(nums,4))