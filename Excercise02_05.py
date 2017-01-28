
class CostInfo():
    def __init__(self, gratuity, cost):
        self.gratuity = gratuity;
        self.cost = cost;

def calculate_total(subtotal,gratuity_rate):
    gratuity_rate = gratuity_rate/100;
    gratuity =  gratuity_rate*subtotal
    subtotal += gratuity
    return  CostInfo(gratuity,subtotal);
def main():
    subtotal, gratuity_rate = eval(input("Enter the subtotal and a gratuity rate: "))
    orderInfo = calculate_total(subtotal,gratuity_rate);
    print("The gratuity is %.2f" % orderInfo.gratuity, "and the total is %.2f" % orderInfo.cost)
if __name__ == '__main__':
    main()

