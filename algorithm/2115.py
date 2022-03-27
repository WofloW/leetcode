# 2115. Find All Possible Recipes from Given Supplies
# https://leetcode.com/problems/find-all-possible-recipes-from-given-supplies/

class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        graph = defaultdict(list)
        indegrees = defaultdict(int)
        for i, v in enumerate(ingredients):
            for required in v:
                graph[required].append(recipes[i])
                indegrees[recipes[i]] += 1

        count = 0

        answer = []
        while supplies:
            done = supplies.pop()
            if graph[done]:
                for recipe in graph[done]:
                    indegrees[recipe] -= 1
                    if indegrees[recipe] == 0:
                        supplies.append(recipe)
                        answer.append(recipe)
        return answer

