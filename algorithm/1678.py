# 1678. Goal Parser Interpretation
# https://leetcode.com/problems/goal-parser-interpretation/

class Solution:
    def interpret(self, command: str) -> str:
        res = []
        i = 0
        while i < len(command):
            c = command[i]
            if c == 'G':
                res.append('G')
                i += 1
            elif c == '(' and command[i + 1] == 'a':
                res.append('al')
                i += 4
            else:
                res.append('o')
                i += 2
        return ''.join(res)

    def interpret2(self, command: str) -> str:
        return command.replace('(al)', 'al').replace('()', 'o')