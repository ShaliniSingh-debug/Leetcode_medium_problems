class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
      

        left, right = 0, len(nums) - 1

        while left < right:
            mid = (left + right) // 2
            # Ensure mid is even
            if mid % 2 == 1:
                mid -= 1

            if nums[mid] == nums[mid + 1]:
                # The pair is valid → single is on the right
                left = mid + 2
            else:
                # Pair is broken → single is on the left (or at mid)
                right = mid

        return nums[left]
        
    # class Solution:
    # def singleNonDuplicate(self, nums: List[int]) -> int:
    #     low = 0
    #     high = len(nums) - 1

    #     while low <= high:
    #         mid = (low + high) // 2

    #         # Edge cases
    #         if mid == 0:
    #             return nums[0] if nums[0] != nums[1] else None
    #         if mid == len(nums) - 1:
    #             return nums[-1] if nums[-1] != nums[-2] else None

    #         if nums[mid] != nums[mid - 1] and nums[mid] != nums[mid + 1]:
    #             return nums[mid]
    #         elif nums[mid] == nums[mid - 1]:
    #             if (mid - 1) % 2 == 0:
    #                 low = mid + 1
    #             else:
    #                 high = mid - 2
    #         else:
    #             if mid % 2 == 0:
    #                 low = mid + 2
    #             else:
    #                 high = mid - 1
