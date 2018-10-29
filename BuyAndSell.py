import random
class BuyAndSell:

	def __init__(self, csp, us):
		self.currentStockPrice = csp
		self.purchaseUnit = 0.0
		self.sellingUnit = 0.0
		self.userStock = us

	def getCurrentStockPrice(self):
		number = random.uniform(-2, 2)
		self.currentStockPrice = self.currentStockPrice + number
		while(self.currentStockPrice<0):
			number = random.uniform(-2, 2)
			self.currentStockPrice = self.currentStockPrice + number
		return self.currentStockPrice

	def purchase(self, unitsToBuy):
		self.userStock = self.userStock + unitsToBuy
		print("It will cost you: $ "+ str(self.getCurrentStockPrice()*unitsToBuy))
		return

	def purchaseSet(self, unitsToBuy):
		self.userStock = self.userStock + unitsToBuy
		return

	def selling(self, unitsToSell):
		self.userStock = self.userStock - unitsToSell
		print("You earn: $ "+str(self.getCurrentStockPrice()*unitsToSell))
		return

	def sellingSet(self, unitsToSell):
		self.userStock = self.userStock - unitsToSell;
		print("You earn: $ "+str(self.getCurrentStockPrice()*unitsToSell))
		return

	def getUserStockUnit(self):
		return self.userStock

	def returnCurrentStockPrice(self):
		return self.currentStockPrice