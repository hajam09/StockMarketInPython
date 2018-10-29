import random
from BuyAndSell import*
class Estates(BuyAndSell):

	def __init__(self, pt, csu, csp, us):
		super().__init__(csp, us)
		self.propertyType = pt
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
		number = random.uniform(-600, 600)
		self.currentStockPrice = self.currentStockPrice + number
		while(self.currentStockPrice<0):
			number = random.uniform(-600, 600)
			self.currentStockPrice = self.currentStockPrice + number
		return self.currentStockPrice

	def getStockName(self):
		return self.propertyType

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