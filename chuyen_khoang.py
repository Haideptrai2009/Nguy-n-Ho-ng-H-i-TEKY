# abstract class: Transaction
# concrete class: CashTransaction, TransaferTransaction, CardTransaction
from abc import ABC, abstractmethod

class Transaction(ABC):     
    def __init__(self,thoi_gian,ten,gia_tri): 
        self.thoi_gian = thoi_gian
        self.ten = ten
        self.gia_tri = gia_tri
class CashTransaction(Transaction):
    def lay_thoi_gian(self): 
        return self.thoi_gian
    def lay_ten(self): 
        return self.ten
    def lay_gia_tri(self): 
        return self.gia_tri
class TransferTransaction(Transaction):
    def lay_thoi_gian(self): 
        return self.thoi_gian
    def lay_ten(self): 
        return self.ten
    def lay_gia_tri(self): 
        return self.gia_tri
class CardTransaction(Transaction):
    def lay_thoi_gian(self): 
        return self.thoi_gian
    def lay_ten(self): 
        return self.ten
    def lay_gia_tri(self): 
        return self.gia_tri
    
cash_trans = CashTransaction('2025-03-02 22:00:00','admin',20000)
tf_trans = TransferTransaction('2025-03-01 14:00:00','admin',45000)
card_trans = CardTransaction('2025-03-02 10:00:00','tung',50000)

transaction_list = [cash_trans, tf_trans, card_trans]
for trans in transaction_list:
    print(trans)

def getHighestValue(trans_list):
    pass

getHighestValue(transaction_list)

def getHighestValueByUser(trans_list, user):
    pass

getHighestValueByUser(transaction_list,'admin')

def getTransactionByDate(trans_list, date):
    pass

getTransactionByDate(transaction_list, '2025-03-02')

def export(trans_list):
    pass

export(transaction_list)