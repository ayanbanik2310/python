class Shop:
    shopping_mall = 'bashundhara'        # class attribute
    # cart = []                          # class attribute
    def __init__(self, buyer):
        self.buyer = buyer
        self.cart = []                 # instance attribute
    
    def add_to_cart(self, item):
        self.cart.append(item)
    
buyer1 = Shop('ayan')
buyer1.add_to_cart('shoe')
buyer1.add_to_cart('shirt')

print(buyer1.buyer, ':' ,buyer1.cart)


buyer2 = Shop('antar')
buyer2.add_to_cart('book')
buyer2.add_to_cart('watch')

print(buyer2.buyer, ':' ,buyer2.cart)


buyer3 = Shop('she')
buyer3.add_to_cart('ear-phone')
buyer3.add_to_cart('ice-cream')
buyer3.add_to_cart('mobile')

print(buyer3.buyer, ':' ,buyer3.cart)



