from collections import deque


class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        sortedDeck = deque(sorted(deck))
        res = deque([])

        res.append(sortedDeck.pop())

        while len(sortedDeck) > 0:
            el = sortedDeck.pop()

            x = res.pop()
            res.appendleft(x)
            res.appendleft(el)
        return list(res)
