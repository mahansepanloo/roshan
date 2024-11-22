from products.models import ProductsModel


class Cart:
    def __init__(self,request):
        self.session = request.session
        cart = self.session.get('cart')
        if not cart:
            cart = self.session['cart']={}
        self.cart = cart


    def Total_price(self):
        return (sum(item['total_price'] for item in self.cart.values()))



    def add(self, product, quantity):
        product_id = str(product.id)
        if not product_id in self.cart:
            self.cart[product_id] = {
                'quantity' : 0,
                'price' : str(product.price)
            }
        self.cart[product_id]['quantity'] += quantity
        self.session.modified = True

    def remove(self, product, quantity):
        product_id = str(product.id)
        if  product_id in self.cart:
            self.cart[product_id]['quantity'] -= quantity
        self.session.modified = True

    def remove_product(self,product):
        product_id = str(product.id)
        if product_id in self.cart:
            del self.cart[product_id]
            self.session.modified =True



    def clear(self):
        del self.session['cart']
        self.session.modified =True