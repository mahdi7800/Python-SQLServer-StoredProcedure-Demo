class Validation :
    def validation_py (self,customer_id , amount):

        if len(customer_id) != 5:
            print("Customer ID must be 5 characters.")
            return False

        if customer_id.strip() == "":
            print("Customer ID cannot be an empty string.")
            return False

        if amount.strip() == "":
            print("Amount cannot be an empty string.")
            return False

        try :
            float(amount)
        except ValueError:
            print("Please enter a valid amount.")
            return False

        return True
    def validation_report_invoice (self,customer_id , orderid):
        if customer_id.strip() == "":
            print("Customer ID cannot be an empty string.")
            return False
        if len(customer_id) != 5:
            print("Customer ID must be 5 characters.")
            return False
        if orderid.strip() == "":
            print("Order ID cannot be an empty string.")
            return False

        try:
            int(orderid)
        except Exception as error :
            print("Order ID must be an integer.")
            return False

        return True
