from datetime import datetime
import db.database as db

database = db.Database()

def main():

    customer_id = input("Enter Customer ID: ")
    amount = input("Enter Amount: ")


    try :
        PaymentDate = datetime.now()
        sql = """ 
                    DECLARE @Result NVARCHAR(100);
                    EXEC usp_CutomerPayment
                    @CustomerID=?,
                    @Amount=?,
                    @PaymentDate=?,
                    @Resualt=@Result OUTPUT;
                    SELECT @Result 
                    """
        database.execute_stored_procedure(sql , customer_id, amount,PaymentDate)
        result = database.fach_one()[0]
        database.commit()
        print(result)
    except Exception as error :
        database.rollback()
        print(f"Database Error: {error}")
    finally:
        database.close()



main()