# 1410. HTML Entity Parser
# https://leetcode.com/problems/html-entity-parser/

class Solution:
    def entityParser(self, text: str) -> str:
        original = ['&quot;', '&apos;', '&gt;', '&lt;', '&frasl;', '&amp;']
        to = ['"', "'", '>', '<', '/', '&']

        for i in range(len(original)):
            text = text.replace(original[i], to[i])

        return text