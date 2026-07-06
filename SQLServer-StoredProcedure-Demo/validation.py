def validation (customer_id , amount):

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