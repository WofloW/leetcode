
class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits:
            return []
        
        result = []
        combination = []
        mapping = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }
        self.dfs(0, mapping, digits, combination, result)
        return result
    
    def dfs(self, index, mapping, digits, combination, result):
        if index == len(digits):
            result.append(''.join(combination))
            return
        
        current_char_list = mapping[digits[index]]
        for i in range(len(current_char_list)):
            char = current_char_list[i]
            combination.append(char)
            self.dfs(index + 1, mapping, digits, combination, result)
            combination.pop()
            
            
'''
Algorithm:
DFS

Notice:
Edge case: 0, 1
'''
