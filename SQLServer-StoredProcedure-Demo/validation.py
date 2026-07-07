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

   def validate_update(self, employee_id, last_name=None, first_name=None, birth_date=None, city=None, country=None,
                        title_of_courtesy=None):
        if employee_id.strip() == "":
            print("Employee ID is required")
            return False
        try:
            int(employee_id)
        except Exception as error:
            print("Employee ID must be a number")
            return False

        if last_name is not None:
            if last_name.isdigit():
                print("last_name cannot be a number")
                return False
        if first_name is not None:
            if first_name.isdigit():
                print("first_name cannot be a number")
                return False
        if birth_date is not None:
            try:
                datetime.strptime(birth_date, "%Y-%m-%d")
            except Exception as error:
                print("BirthDate format is invalid")
                return False
        if city is not None:
            if city.isdigit():
                print("City cannot be a number")
                return False
        if country is not None:
            if country.isdigit():
                print("Country cannot be a number")
                return False
        if title_of_courtesy is not None:
            if title_of_courtesy.isdigit():
                print("TitleOfCourtesy cannot be a number")
                return False

        return True

    def validate_insert( self, last_name, first_name, birth_date, city=None, country=None, title_of_courtesy=None):

        if last_name.strip() == "":
            print("LastName is required")
            return False
        if first_name.strip() == "":
            print("FirstName is required")
            return False
        if birth_date.strip() == "":
            print("BirthDate is required")
            return False

        try:
            datetime.strptime(birth_date, "%Y-%m-%d")
        except ValueError:
            print("BirthDate format is invalid. Use YYYY-MM-DD")
            return False

        if city is not None:
            if city.isdigit():
                print("City cannot be a number")
                return False
        if country is not None:
            if country.isdigit():
                print("Country cannot be a number")
                return False
        if title_of_courtesy is not None:
            if title_of_courtesy.isdigit():
                print("TitleOfCourtesy cannot be a number")
                return False

        return True

    def validate_delete( self, employee_id):
        if employee_id.strip() == '':
            print("Employee ID is required")
            return False
        try:
            int(employee_id)
        except Exception as error:
            print(f"{error}")
            return False
        return True


        return True
