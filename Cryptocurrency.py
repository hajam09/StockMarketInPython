import random
from BuyAndSell import*
class Cryptocurrency(BuyAndSell):

	def __init__(self, cn, csu, csp, us):
		super().__init__(csp, us)
		self.currencyName = cn
		self.currentStockUnit = csu

	def productInfo(self):
		productName = "Product name is: "
		stockPrice = "Current stock price is: $ "
		stockUnit = "Current stock unit left is: "

		print(productName + self.getStockName())
		print(stockPrice + str(self.getCurrentStockPrice()))
		print(stockUnit+str(self.getCurrentStockUnit()))
		print()
		return

	def getCurrentStockPrice(self):
		currentStockPrice = self.returnCurrentStockPrice()
		number = random.uniform(-400, 400)
		self.currentStockPrice = self.currentStockPrice + number
		while(self.currentStockPrice<0):
			number = random.uniform(-400, 400)
			self.currentStockPrice = self.currentStockPrice + number
		return self.currentStockPrice

	def getStockName(self):
		return self.currencyName

	def getCurrentStockUnit(self):
		return self.currentStockUnit

	def purchase(self, unitsToBuy):
		self.purchaseSet(unitsToBuy)
		self.currentStockUnit = self.currentStockUnit - unitsToBuy
		return

	def selling(self, unitsToSell):
		self.sellingSet(unitsToSell)
		self.currentStockUnit = self.currentStockUnit + unitsToSell
		return