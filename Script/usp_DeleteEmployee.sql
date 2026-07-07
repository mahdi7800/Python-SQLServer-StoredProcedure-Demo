USE Northwind;
GO 


CREATE OR ALTER PROC usp_DeleteEmployee @EmployeeID int
AS 
BEGIN 
    SET NOCOUNT ON;
	SET XACT_ABORT ON;
	   BEGIN TRY 
          IF EXISTS (SELECT EmployeeID FROM Orders WHERE EmployeeID IN (@EmployeeID))
                 BEGIN 
                    RAISERROR(N'One or more employees have orders and cannot be deleted.',16,1);
                    RETURN;
                 END
                DELETE FROM Employees 
                WHERE EmployeeID = @EmployeeID
                IF @@ROWCOUNT = 0 
                 BEGIN 
                     RAISERROR(N'Employee not found.',16,1);
                     RETURN;
                 END
	   END TRY
	   BEGIN CATCH
           DECLARE @ErrorMessage nvarchar(4000) = ERROR_MESSAGE();
           DECLARE @ErrorSeverity int = ERROR_SEVERITY();
           DECLARE @ErrorState int  =  ERROR_STATE();
           SELECT ERROR_PROCEDURE() AS ErrorProcedure;
           RAISERROR (@ErrorMessage,@ErrorSeverity,@ErrorState);
	   END CATCH
END


-- EXECUTE usp_DeleteEmployee @EmployeeID = @EmployeeID