'''Super () example'''

class UPI:
    def Payment_UPI(self):
        print('Applying UPI payment logic')

class PhonePay(UPI):
    def payment(self):
        print('Paying through Phone pay')
        super().Payment_UPI()
        print('Payment Completed')

x = PhonePay()
x.payment()