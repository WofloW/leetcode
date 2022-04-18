# 1773. Count Items Matching a Rule
# https://leetcode.com/problems/count-items-matching-a-rule/

MAPPING = {'type': 0, 'color': 1, 'name': 2}

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        return sum(1 for item in items if item[MAPPING[ruleKey]] == ruleValue)
