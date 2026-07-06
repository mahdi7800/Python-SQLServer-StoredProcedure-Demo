USE Northwind;
GO 

CREATE OR ALTER FUNCTION dbo.fn_GetOrderTotal(@CustomerID nchar(5) , @OrderID int)
RETURNS money
AS 
BEGIN 
     DECLARE @Total money; 

     SELECT @Total = CONVERT(money ,SUM ((OD.Quantity * OD.UnitPrice) * (1 - OD.Discount))) 
     FROM Customers AS C INNER JOIN Orders AS O ON C.CustomerID = O.CustomerID
                         INNER JOIN [Order Details] AS OD ON O.OrderID = OD.OrderID
     WHERE O.CustomerID = @CustomerID AND OD.OrderID = @OrderID
    

     RETURN ISNULL(@Total,0)
     
END

GO 