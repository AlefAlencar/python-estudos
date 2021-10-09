"""
Alguns exemplos sobre ITERADORES do  canal gringo "Socratica"
"""

'''# iterar com loops
usernames = ('Rainer', 'Alfons', 'Flatsheep')
looper = iter(usernames)
while True:
    try:
        user = next(looper)
        print(user)
    except StopIteration:
        break  # '''


# iterar com
class Portfolio:
    def __init__(self):
        self.holdings = {}

    def buy(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) + shares

    def sell(self, ticker, shares):
        self.holdings[ticker] = self.holdings.get(ticker, 0) - shares

    def __iter__(self):
        return iter(self.holdings.items())


p = Portfolio()
p.buy('ALPHA', 15)
p.buy('BETA', 23)
p.buy('GAMMA', 9)
p.buy('GAMMA', 20)

for (ticker, shares) in p:
    print(ticker, shares)  # '''

'''import itertools

ranks = list(range(2, 11)) + ['J', 'Q', 'K', 'A']
ranks = [str(rank) for rank in ranks]

suits = ['Hearts', 'Clubs', 'Diamons', 'Spades']
deck = [card for card in itertools.product(ranks, suits)]

hands = [hand for hand in itertools.combinations(deck, 5)]

print(f'The number of 5-card poker hands is {len(hands)}.')  # '''
