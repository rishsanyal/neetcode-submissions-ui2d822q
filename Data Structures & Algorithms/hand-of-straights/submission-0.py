class Solution(object):
    def isNStraightHand(self, hand, groupSize):
        """
        :type hand: List[int]
        :type groupSize: int
        :rtype: bool
        """

        # MAX - HEAP with count
        c = Counter(hand)
        h = [(i,j) for (i,j) in c.items()]

        heapq.heapify_max(h)
        
        res = []

        while h:
            temp_res = []
            remaining_cards = []
            prev_card = None

            for _ in range(groupSize):
                if not h:
                    return False

                card, card_count = heapq.heappop_max(h)

                if prev_card and prev_card != card+1:
                    return False
                    
                prev_card = card

                if card_count-1 > 0:
                    remaining_cards.append((card, card_count-1))
                
                temp_res.append(card)

            for card, card_count in remaining_cards:
                heapq.heappush_max(h, (card, card_count))

            res.append(temp_res)

        return True