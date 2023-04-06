#!/usr/bin/env python3


# https://www.w3resource.com/python-exercises/list/python-data-type-list-exercise-257.php

def check_same_contents(nums1, nums2):
  for x in set(nums1 + nums2):
    if nums1.count(x) != nums2.count(x):
      return False
  return True

nums1 = [1, 2, 4]
nums2 = [2, 4, 1]
print("Original list elements:")
print(nums1)
print(nums2)
print("\nCheck two said lists contain the same elements regardless of order!")
print(check_same_contents(nums1, nums2))
nums1 = [1, 2, 3]
nums2 = [1, 2, 3]
print("\nOriginal list elements:")
print(nums1)
print(nums2)
print("\nCheck two said lists contain the same elements regardless of order!")
print(check_same_contents(nums1, nums2))
nums1 = [1, 2, 3]
nums2 = [1, 2, 4]
print("\nOriginal list elements:")
print(nums1)
print(nums2)
print("\nCheck two said lists contain the same elements regardless of order!")
print(check_same_contents(nums1, nums2))
