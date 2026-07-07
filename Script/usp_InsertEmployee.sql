USE Northwind;
GO 

CREATE OR ALTER PROC usp_InsertEmployee @LastName nvarchar(20) , @FirstName nvarchar(10), @BirthDate datetime, @City nvarchar(15) = NULL  , @Country nvarchar(15) = NULL , @TitleOfCourtesy nvarchar(25) = NULL , @NewEmployeeID int OUTPUT
AS 
BEGIN
   SET NOCOUNT ON;
   SET XACT_ABORT ON;

     BEGIN TRY
          DECLARE @FirstNameNew nvarchar(10); 
              SET @FirstNameNew = UPPER(LEFT(@FirstName,1))+LOWER(SUBSTRING(@FirstName,2,LEN(@FirstName)));
          DECLARE @LastNameNew nvarchar(20); 
              SET @LastNameNew = UPPER(LEFT(@LastName,1))+LOWER(SUBSTRING(@LastName,2,LEN(@LastName)));
          DECLARE @CityNew nvarchar(15);
              SET @CityNew = UPPER(LEFT(@City,1))+LOWER(SUBSTRING(@City,2,LEN(@City)));
          DECLARE @CountryNew nvarchar(15);
              SET @CountryNew = UPPER(LEFT(@Country,1))+LOWER(SUBSTRING(@Country,2,LEN(@Country)));
          INSERT INTO Employees (FirstName , LastName , TitleOfCourtesy , BirthDate , Country ,City)
              VALUES (@FirstNameNew , @LastNameNew , @TitleOfCourtesy , @BirthDate , @CountryNew , @CityNew)
          SET @NewEmployeeID = SCOPE_IDENTITY()
     END TRY 
     BEGIN CATCH 
           DECLARE @ErrorMessage nvarchar(4000) = ERROR_MESSAGE();
           DECLARE @ErrorSeverity int = ERROR_SEVERITY();
           DECLARE @ErrorState int  =  ERROR_STATE();
           SELECT ERROR_PROCEDURE() AS ErrorProcedure;
           RAISERROR (@ErrorMessage,@ErrorSeverity,@ErrorState);
     END CATCH
END

-- EXECUTE usp_InsertEmployee @LastName = @LastName , @FirstName = @FirstName , @BirthDate = @BirthDate, @City  = @City   , @Country  = @Country , @TitleOfCourtesy = @TitleOfCourtesy