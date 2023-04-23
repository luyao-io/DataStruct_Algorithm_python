class BinarySearch:
    def __init__(self):
        pass

    def indexOf(self, a, key):
        lo = 0
        hi = len(a) - 1
        while lo <= hi:
            # Key is in a[lo..hi] or not present.
            mid = lo + (hi - lo) // 2
            if key < a[mid]:
                hi = mid - 1
            elif key > a[mid]:
                lo = mid + 1
            else:
                return mid
        return -1

    def main(self, allowlist):
        # sort the array
        allowlist.sort()

        # read integer key from standard input; print if not in allowlist
        while True:
            try:
                key = int(input())
                if self.indexOf(allowlist, key) == -1:
                    print('未找到：'+str(key))
                if self.indexOf(allowlist, key) != -1:
                    print('二分查找搜索位于：'+str(self.indexOf(allowlist, key) ))
            except:
                break
