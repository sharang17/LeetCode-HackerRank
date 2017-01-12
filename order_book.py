# a simple orderbook class                                                                                            
class OrderBook:
    def __init__(self):
        self.orders={}
    def buy(self, order_id, price):
        temp_dict={(order_id,price)}
        self.orders.update(temp_dict)
        print self.orders
        
    def sell(self, order_id):
        if order_id not in self.orders:
            return ""
        else:
            del self.orders[order_id]                                                                                              

    def get_high_price(self):
        if bool(self.orders)==False:
            print "Entered"
            return -1
        else:
            high=max(self.orders,key=self.orders.get)
            val=self.orders.get(high)
            return val


book = OrderBook()

input_txt = "0 B 1 10"
elements=input_txt.split(" ")
time_order = int(elements[0])
type_order = elements[1]
id_order = int(elements[2])
price_order = None
if len(elements) == 4:
    price_order = float(elements[3])
if type_order=="B":
    book.buy(id_order,price_order)
    high=str(book.get_high_price())
    print str(time_order)+" "+high
else:
    book.sell(id_order)
    high=str(book.get_high_price())
    print str(time_order)+" "+high
