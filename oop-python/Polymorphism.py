'''Polymorphism example code'''

class UPI:
    def payment_gateway(self):
        print('UPI Gateway')

class PhonePay(UPI):
    def payment_gateway(self):
        print('Payment through PhonePay UPI gateway')

class GooglePay(UPI):
    def payment_gateway(self):
        print('Payment Through Google pay Gateway')

'''Method Over riding'''
obj = [UPI(),PhonePay(), GooglePay()]

for ref in obj:
    ref.payment_gateway()