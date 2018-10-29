from StockMarket import*
from Cryptocurrency import*
from Estates import*

class MainClass:
	def __init__(self):

		s1 = StockMarket("gold", 5000.0, 2.50, 0)
		s2 = StockMarket("silver", 6500.0, 5.50, 0)
		s3 = StockMarket("bronze", 7500.0, 5.75, 0)

		c1 = Cryptocurrency("bitcoin", 8.0, 6500.0, 0)
		c2 = Cryptocurrency("ethereum", 11.0, 4500.0, 0)
		c3 = Cryptocurrency("litecoin", 15.0, 5050.0, 0)

		e1 = Estates("flat", 9500.0, 145276.0, 0)
		e2 = Estates("detached", 9000.0, 278432.0, 0)
		e3 = Estates("cottage", 500.0, 205435.0, 0)

		items1 = [s1, s2, s3]
		items2 = [c1, c2, c3]
		items3 = [e1, e2, e3]

		choice = input("Do you want to go for Stock Market (stock) or Cryptocurrency (crypto) or Estates Properties (estate) or quit? ").lower()

		while(choice!="quits"):
			if(choice=="stock"):
				self.stock(items1)
			elif(choice=="crypto"):
				self.crypto(items2)
			elif(choice=="estate"):
				self.estate(items3)

			choice = input("Do you want to go for Stock Market (stock) or Cryptocurrency (crypto) or Estates Properties (estate) or quit? ").lower()


	def stock(self, items):
		for i in range(len(items)):
			items[i].productInfo()

		choice = input("Do you want to buy or sell shares or back? ").lower()

		while(choice!="back"):
			if(choice=="buy"):
				self.stockBuyMethod(items)
			elif(choice=="sell"):
				self.stockSellMethod(items)

			choice = input("Do you want to buy or sell shares or back? ").lower()

		if(choice=="back"):
			return

	def crypto(self,items):
		for i in range(len(items)):
			items[i].productInfo()

		choice = input("Do you want to buy or sell shares or back? ").lower()

		while(choice!="back"):
			if(choice=="buy"):
				self.cryptoBuyMethod(items)
			elif(choice=="sell"):
				self.cryptoSellMethod(items)

			choice = input("Do you want to buy or sell shares or back? ").lower()

		if(choice=="back"):
			return

	def estate(self, items):
		for i in range(len(items)):
			items[i].productInfo()

		choice = input("Do you want to buy or sell shares or back? ").lower()

		while(choice!="back"):
			if(choice=="buy"):
				self.estateBuyMethod(items)
			elif(choice=="sell"):
				self.estateSellMethod(items)

			choice = input("Do you want to buy or sell shares or back? ").lower()

		if(choice=="back"):
			return

	def stockBuyMethod(self, items):
		for i in range(len(items)):
			items[i].productInfo()

		choice = input("What do you want to buy from list? ").lower()

		for j in range(len(items)):
			if(choice==items[j].stockName):
				try:
					unitstoBuy = float(input("How much "+ (items[j]).getStockName()+" do you want to buy? "))

					while(unitstoBuy>items[j].getCurrentStockUnit()):
						unitstoBuy = float(input("Not enough stocks left, enter again: "))

					items[j].purchase(unitstoBuy)

					for k in range(len(items)):
						items[k].productInfo()

					break
				except:
					print("Cannot enter String for purchasing units. So enter an Integer or double.")
					self.stockBuyMethod(items)
		return


	def stockSellMethod(self, items):
		print("Below are the Stock shares you own.")
		for i in range(len(items)):
			print(items[i].getStockName()+" = "+str(items[i].getUserStockUnit()))

		choice = input("What do you want to sell from list? ")

		for j in range(len(items)):
			if(choice==str(items[j].stockName)):
				try:
					unitstoSell = float(input("How much "+ items[j].getStockName()+" do you want to sell? "))

					while(unitstoSell>items[j].getUserStockUnit() and unitstoSell >0):
						unitstoSell = float(input("Not enough stocks left, enter again: "))

					items[j].selling(unitstoSell)

					for k in range(len(items)):
						items[k].productInfo()

					#break
				except:
					print("Cannot enter String for selling units. So enter an Integer or double.")
					self.stockSellMethod(items)

	def cryptoBuyMethod(self, items):
		for i in range(len(items)):
			items[i].productInfo()

		choice = input("What do you want to buy from list? ").lower()

		for j in range(len(items)):
			if(choice==(items[j].currencyName)):
				try:
					unitstoBuy = float(input("How much "+ (items[j]).getStockName()+" do you want to buy? "))

					while(unitstoBuy>items[j].getCurrentStockUnit()):
						unitstoBuy = float(input("Not enough stocks left, enter again: "))

					items[j].purchase(unitstoBuy)

					for k in range(len(items)):
						items[k].productInfo()

					break
				except:
					print("Cannot enter String for purchasing units. So enter an Integer or double.")
					self.cryptoBuyMethod(items)
		return

	def cryptoSellMethod(self, items):
		print("Below are the Stock shares you own.")
		for i in range(len(items)):
			print(items[i].getStockName()+" = "+str(items[i].getUserStockUnit()))

		choice = input("What do you want to sell from list? ")

		for j in range(len(items)):
			if(choice==str((items[j].currencyName))):
				try:
					unitstoSell = float(input("How much "+ items[j].getStockName()+" do you want to sell? "))

					while(unitstoSell>items[j].getUserStockUnit() and unitstoSell >0):
						unitstoSell = float(input("Not enough stocks left, enter again: "))

					items[j].selling(unitstoSell)

					for k in range(len(items)):
						items[k].productInfo()

					break
				except:
					print("Cannot enter String for selling units. So enter an Integer or double.")
					self.cryptoSellMethod(items)

	def estateBuyMethod(self, items):
		for i in range(len(items)):
			items[i].productInfo()

		choice = input("What do you want to buy from list? ").lower()

		for j in range(len(items)):
			if(choice==(items[j].propertyType)):
				try:
					unitstoBuy = float(input("How much "+ (items[j]).getStockName()+" do you want to buy? "))

					while(unitstoBuy>items[j].getCurrentStockUnit()):
						unitstoBuy = float(input("Not enough stocks left, enter again: "))

					items[j].purchase(unitstoBuy)

					for k in range(len(items)):
						items[k].productInfo()

					break
				except:
					print("Cannot enter String for purchasing units. So enter an Integer or double.")
					self.estateBuyMethod(items)
		return

	def estateSellMethod(self, items):
		print("Below are the Stock shares you own.")
		for i in range(len(items)):
			print(items[i].getStockName()+" = "+str(items[i].getUserStockUnit()))

		choice = input("What do you want to sell from list? ")

		for j in range(len(items)):
			if(choice==items[j].propertyType):
				try:
					unitstoSell = float(input("How much "+ items[j].getStockName()+" do you want to sell? "))

					while(unitstoSell>items[j].getUserStockUnit() and unitstoSell >0):
						unitstoSell = float(input("Not enough stocks left, enter again: "))

					items[j].selling(unitstoSell)

					for k in range(len(items)):
						items[k].productInfo()

					break
				except:
					print("Cannot enter String for selling units. So enter an Integer or double.")
					self.estateSellMethod(items)
