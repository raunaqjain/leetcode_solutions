class TrieNode:
    def __init__(self):
        self.end = False
        self.children = dict()
        
class Trie:
    def __init__(self):
        self.trie = TrieNode()
    
    def insert(self, word):
        curr = self.trie
        for ch in word:
            if ch not in curr.children:
                curr.children[ch] = TrieNode()
            curr = curr.children[ch]
            
        curr.end = True
            

class Solution:
    def findWords(self, board: List[List[str]], words: List[str]) -> List[str]:
        def dfs(board, i, j, node, ans,out):
            if node.end:
                out.append(ans)
                node.end = False
                
            if i < 0 or i >= M or j < 0 or j >= N:
                return
            
            tmp = board[i][j]
            node = node.children.get(tmp)
            if not node:
                return
            board[i][j] = "$"
            dfs(board, i-1, j, node, ans+tmp, out)
            dfs(board, i+1, j, node, ans+tmp, out)
            dfs(board, i, j-1, node, ans+tmp, out)
            dfs(board, i, j+1, node, ans+tmp, out)
            
            board[i][j] = tmp
            
        
        trie = Trie()
        node = trie.trie
        for word in words:
            trie.insert(word)
            
        out = []
        M, N = len(board), len(board[0])
        for i in range(M):
            for j in range(N):
                dfs(board, i, j, node, "", out)  
        
        return out
