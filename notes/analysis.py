''' Learn how to analysis data with list-comprehensions:

List Comprehensions:  [instructions to make the list]

Syntax:
-------
 [<expr> for <var> in <iterable>]
 [<expr> for <var> in <iterable> if <cond>]

Code Organization:
------------------
1 Acquire your data and convert it to a convenient form
2 Analyze your data
3 Format your output

'''

import portfolio
from pprint import pprint

port = portfolio.get_portfolio('notes/stocks.txt')
pprint(port)

print 'Simple projections (subsets of columns)'
print [trade.symbol for trade in port]
print [trade.shares for trade in port]
print [trade.price for trade in port]

print 'Which securities have you bought?'
print 'SELECT DISTINCT symbol FROM Port ORDER BY symbol;'
print sorted(set([trade.symbol for trade in port]))

print 'Cumulatively, how many shares of Cisco have you bought?'
print 'SELECT SUM(shares) FROM Port WHERE symbol = "CSCO";'
print sum([t.shares for t in port if t.symbol == 'CSCO'])

print 'How much money did you invest in the market?'
print 'SELECT SUM(shares * price) FROM Port;'
print sum([trade.shares * trade.price for trade in port])
