import json
import random
from collections import OrderedDict
from bottledaemon import daemon_run
from bottle import run, route, request

# remove private properties from json output
def default_json(instance):
    return {k: v
            for k, v in vars(instance).items()
            if not str(k).startswith('_')}


# the card itself with all random values filled
class Card:
	def __init__(self):
		self._colname = 'BINGO'
		self._line_step = 15
		self.columns = OrderedDict()
		self._randomize()

	# fulfill one line of values
	def _new_line(self, line):
		# range control for each line
		rang = (self._line_step * line)
		values = []
		for i in range(5):
			# get unique random #
			nval = random.randint(rang, rang + self._line_step)
			while nval in values:
				nval = random.randint(rang, rang + self._line_step)
			# add new value to the card line
			values.append( nval )
		return values

	# generate the random values for this card
	def _randomize(self):
		count = 0
		for l in self._colname:
			# create each line of random numbers for this card
			self.columns[l] = self._new_line(count)
			# -1 the value of center position
			if (l == 'N'):
				self.columns[l][2] = -1
			count += 1

# deal to manage all cards requested by client
class Deal:
	# construct all cards requested by client
	def __init__(self, cards):
		self._num_cards = cards
		self.cards = []
		# generate cards
		self._randomize()

	# generate random cards for the # of cards requested
	def _randomize(self):
		for c in range(self._num_cards):
			self.cards.append( Card() )

	# return the json representation of the deal
	def json(self):
		return json.dumps(self, default=default_json, sort_keys=False, indent=4)


# deal service
@route('/deal')
def deal():
	# default # of cards is 2
	cards = 2
	try:
		cards = int(request.query.cards)
	except ValueError:
		# parameter error, return default # of cards
		print 'Number of cards not an integer value. Returning 2 cards.'
	deal = Deal(cards)
	return deal.json()


if __name__ == "__main__":
	daemon_run(host='0.0.0.0', port=8080)