def check_payments(logfile):
    my_file = open(logfile, "r")
    melon_cost = 1.00
    
    for line in my_file:
        line = line.strip()
        words = line.split(",")
        customer_name = words[1]
        customer_melons = int(words[2])
        customer_paid = float(words[3])
        expected_payment = customer_melons * melon_cost
        
        if expected_payment != customer_paid:
                    print customer_name, "paid %.2f, expected %.2f" % (customer_paid, expected_payment)
                    

def main():
    check_payments("customer_orders.csv")
    

if __name__ == "__main__":
    main()
