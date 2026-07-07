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
def ProcessEmployeeOperation() :
    select_operation = input("\n Select Operation: \n 1: Insert \n 2: Update \n 3: Delete \n")

    sql = """
    DECLARE @Result nvarchar(200);
    EXEC usp_InsertEmployeeAndUpdateAndDelete @type = ?  , 
                                                      @LastName = ?  , 
                                                      @FirstName = ?  ,
                                                      @BirthDate = ?  , 
                                                      @City = ?  , 
                                                      @Country = ?  , 
                                                      @TitleOfCourtesy = ?  , 
                                                      @EmployeeID = ?  , 
                                                      @Result = @Result OUTPUT
                                                      SELECT @Result 
                                                      """
    try:
        if select_operation == "2" or select_operation.lower() == "u" or select_operation.lower() == "update":
            operation_type = "u"
            select_employee_id = input("\n Select Employee ID : ")
            LastName = input("\n Enter LastName (Press Enter to skip): ") or None
            FirstName = input("\n Enter FirstName (Press Enter to skip): ") or None
            BirthDate = input("\n Enter BirthDate YYYY-MM-DD (Press Enter to skip): ") or None
            City = input("\n Enter City (Press Enter to skip): ") or None
            Country = input("\n Enter Country (Press Enter to skip): ") or None
            TitleOfCourtesy = input("\n Enter TitleOfCourtesy (Press Enter to skip): ") or None
            if Validation.validate_update(select_employee_id, LastName, FirstName, BirthDate, City, Country, TitleOfCourtesy):
                employee_id = int(select_employee_id)
                if BirthDate:
                    birth_date = datetime.strptime(BirthDate, "%Y-%m-%d")
                else:
                    birth_date = None
                database.execute_stored_procedure(sql, operation_type, LastName, FirstName, birth_date, City, Country, TitleOfCourtesy,
                               employee_id)
                result = database.fach_one()[0]
                database.commit()
                print(result)
            else:
                print("error update")
        elif select_operation == "1" or select_operation.lower() == "i" or select_operation.lower() == "insert":
            operation_type = "i"
            LastName = input("\n Enter LastName:  ")
            FirstName = input("\n Enter FirstName:")
            BirthDate = input("\n Enter BirthDate:")
            City = input("\n Enter City (Press Enter to skip): ") or None
            Country = input("\n Enter Country (Press Enter to skip): ") or None
            TitleOfCourtesy = input("\n Enter TitleOfCourtesy (Press Enter to skip): ") or None
            select_employee_id = None
            if Validation.validate_insert(LastName, FirstName, BirthDate, City, Country, TitleOfCourtesy):
                birth_date = datetime.strptime(BirthDate, "%Y-%m-%d")
                database.execute_stored_procedure(sql, operation_type, LastName, FirstName, birth_date, City, Country, TitleOfCourtesy,
                               select_employee_id)
                result = database.fach_one()[0]
                print(result)
                database.commit()
            else:
                print("Insert error")
        elif select_operation == "3" or select_operation.lower() == "d" or select_operation.lower() == "delete":
            operation_type = "d"
            LastName = None
            FirstName = None
            BirthDate = None
            City = None
            Country = None
            TitleOfCourtesy = None
            select_employee_id = input("\n Select Employee ID : \n ")
            if Validation.validate_delete(select_employee_id):
                employee_id = int(select_employee_id)
                database.execute_stored_procedure(sql, operation_type, LastName, FirstName, BirthDate, City, Country, TitleOfCourtesy,
                               employee_id)
                result = database.fach_one[0]
                print(result)
                database.commit()
            else:
                print("Employee ID is invalid")
        else:
            print("invalid input")
    except Exception as error:
        print(f"Database Error: {error}")
        database.rollback()
    finally:
        database.close()
        database.close()
        
def main():
    print("1. Payment")
    print("2. Invoice")
    print("3. Report Invoice")
    print("4. Exit")

    choice = input("Select: ")

    if choice == "1":
        payment()

    elif choice == "2":
        report_invoice()

    elif choice == "3":
        ProcessEmployeeOperation()
    elif choice == "4":
        sys.exit()
    else:
        print("Invalid option")

main()

