class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:

        def div(x: int) -> float:
            return x / 2

        _remove = None

        for i in range(len(arr)):
            if arr[i] == 0:
                if _remove:
                    return True
                
                _remove = i

        if _remove: arr.pop(_remove)

        arr1 = frozenset(arr)
        arr2 = frozenset(map(div, arr1))

        return bool(arr1.intersection(arr2))
