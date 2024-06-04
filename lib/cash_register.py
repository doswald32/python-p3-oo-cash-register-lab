#!/usr/bin/env python3

class CashRegister:
  def __init__(self, discount=0, total=0):
    self.discount = discount
    self.total = total
    self.items = []
    self.prices = []

  def add_item(self, title, price, quantity=1):
    self.items.extend([title] * quantity)
    self.total += price * quantity
    self.prices.append(price)

  def apply_discount(self):
    self.total = self.total * (1 - (self.discount / 100))
    if self.discount == 0:
      print("There is no discount to apply.")
    else:
      print(f"After the discount, the total comes to ${int(self.total)}.")

  def items_list_without_multiples(self):
    return list(set(self.items))
  
  def items_with_multiples(self):
    return self.items

  def void_last_transaction(self):
    last_price = self.prices.pop()
    self.total -= last_price

  def void_last_transaction_with_multiples(self):
    if len(self.prices) == 0:
      self.total = 0.0
      return self.total
    else:
      return self.total

