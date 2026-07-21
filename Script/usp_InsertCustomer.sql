USE Northwind;
GO 


CREATE OR ALTER PROCEDURE usp_InsertCustomer @CustomerID nchar(5) ,@CompanyName nvarchar(40) , @ContactName nvarchar(30)  = NULL ,@ContactTitle nvarchar(30) = NULL ,@Address nvarchar(60)  = NULL,  @City nvarchar(15) = NULL , @Region nvarchar(15) = NULL , @PostalCode nvarchar(10) = NULL , @Country nvarchar(15)= NULL , @Phone nvarchar(24)= NULL , @Fax nvarchar(24)= NULL , @Result nchar(5) OUTPUT
AS 
BEGIN 
     /*
        Author      : Mahdi Davoodi
        Date        : 2026/07/12
        Procedure   : usp_InsertCustomer
        Description : Insert a new customer into dbo.Customers
    */
  SET NOCOUNT ON;
  SET XACT_ABORT ON;
  BEGIN TRY 
              
          INSERT INTO dbo.Customers(CustomerID,CompanyName,ContactName,ContactTitle,[Address],City,Region,PostalCode,Country,Phone,Fax)
            VALUES (@CustomerID,@CompanyName,@ContactName,@ContactTitle,@Address,@City,@Region,@PostalCode,@Country,@Phone,@Fax)

            SET @Result = @CustomerID
  END TRY 
  BEGIN CATCH 
           DECLARE @ErrorMessage nvarchar(4000) = ERROR_MESSAGE();
           DECLARE @ErrorSeverity int = ERROR_SEVERITY();
           DECLARE @ErrorState int  =  ERROR_STATE();
           SELECT ERROR_PROCEDURE() AS ErrorProcedure;
           RAISERROR (@ErrorMessage,@ErrorSeverity,@ErrorState);
  END CATCH 
END