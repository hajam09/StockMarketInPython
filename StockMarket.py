import random
from BuyAndSell import*
class StockMarket(BuyAndSell):

	def __init__(self, sn, csu, csp, us):
		super().__init__(csp, us)
		self.stockName = sn
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
		number = random.uniform(-3.5, 3.5)
		currentStockPrice = currentStockPrice + number
		while(currentStockPrice<0):
			number = random.uniform(-3.5, 3.5)
			currentStockPrice = currentStockPrice + number
		return currentStockPrice

	def getStockName(self):
		return self.stockName

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