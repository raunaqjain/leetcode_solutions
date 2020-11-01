class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        data = {1: 1, 2: 1, 3: 2, 4: 6, 5: 24, 6: 120, 7: 720, 8: 5040, 9:40320}
        ans = []
        N = [str(i) for i in range(1, n+1)]
        for i in range(1, n+1):
            idx = (k-1) // data[n-i+1]
            ans.append(N.pop(idx))
            k = k % data[n-i+1]
        return "".join(ans)
                
