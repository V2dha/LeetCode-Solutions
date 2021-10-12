class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        arr = nums
        num = target
        def first_position(start, end, arr, num):
            while start <= end:
                mid = (start + end) // 2
                if num > arr[mid]:
                    start = mid + 1
                elif num < arr[mid]:
                    end = mid - 1
                else:
                    if arr[mid-1] == num and mid-1 >= 0:
                        end = mid - 1
                    else:
                        return mid
            return -1

        def last_position(start, end, arr, num):
            while start <= end:
                mid = (start + end) // 2
                if num > arr[mid]:
                    start = mid + 1 
                elif num < arr[mid]:
                    end = mid - 1
                else:
                    if  mid < len(arr)-1 and arr[mid+1] == num:
                        start = mid + 1
                    else:
                        return mid
            return -1

        def first_last_position(arr, num):
            if not arr:
                return [-1, -1]
            if len(arr) == 1:
                return [0, 0] if num == arr[0] else [-1, -1]
            start = 0
            end = len(arr) - 1
            return [first_position(start, end, arr, num), last_position(start, end, arr, num)]
        return first_last_position(arr, num)