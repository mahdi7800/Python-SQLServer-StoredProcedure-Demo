from datetime import datetime
import db.database as db
from validation import *


Validation = Validation()
database = db.Database()


def payment():
    customer_id = input("Enter Customer ID: ")
    Amount = input("Enter Amount: ")

    if Validation.validation_py(customer_id, Amount):
        try:
            PaymentDate = datetime.now()
            amount = float(Amount)
            sql = """ 
                       DECLARE @Result NVARCHAR(100);
                       EXEC usp_CutomerPayment
                       @CustomerID=?,
                       @Amount=?,
                       @PaymentDate=?,
                       @Resualt=@Result OUTPUT;
                       SELECT @Result 
                       """
            database.execute_stored_procedure(sql, customer_id, amount, PaymentDate)
            result = database.fach_one()[0]
            database.commit()
            print(result)
        except Exception as error:
            database.rollback()
            print(f"Database Error: {error}")
        finally:
            database.close()
    else:
        print("Invalid input. Please try again.")
def report_invoice():
        customer_id = input("Enter Customer ID: ")
        order_id = input("Enter Order ID: ")

        if Validation.validation_report_invoice(customer_id, order_id):
            try:
                order_id = int(order_id)
                sql = """execute usp_GetInvoic @CustomerID = ? , @OrderID = ?"""
                database.execute_stored_procedure(sql, customer_id, order_id)
                rows = database.fech_all()
                invoice = []
                for row in rows:
                    invoice.append({
                        "CustomerID": row.CustomerID,
                        "CompanyName": row.CompanyName,
                        "OrderID": row.OrderID,
                        "OrderDate": row.OrderDate,
                        "ProductName": row.ProductName,
                        "Quantity": row.Quantity,
                        "UnitPrice": row.UnitPrice,
                        "LineTotal": row.LineTotal
                    })
                for item in invoice:
                    print(item)
            except Exception as error:
                print(f"Database Error: {error}")
            finally:
                database.close()
        else:
            print("Invalid input. Please try again.")

def main():
    print("1. Payment")
    print("2. Invoice")
    print("3. Exit")

    choice = input("Select: ")

    if choice == "1":
        payment()

    elif choice == "2":
        report_invoice()

    elif choice == "3":
        sys.exit()
    else:
        print("Invalid option")

main()
