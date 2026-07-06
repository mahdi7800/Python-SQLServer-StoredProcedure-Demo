USE Northwind;
GO 

CREATE OR ALTER PROC usp_GetInvoic @CustomerID nchar(5) , @OrderID int 
AS 
BEGIN 
    /* 
        Author    : Mahdi Davoudi
        Date      : 2026-07-06
        Subject   : Retrieve customer invoice details with line items and grand total.
        Version   : 1.0.0
    */

    SET NOCOUNT ON;
    SET XACT_ABORT ON; 

    
         SELECT C.CustomerID , C.CompanyName , O.OrderID ,O.OrderDate,  P.ProductName , OD.Quantity ,OD.UnitPrice,Convert(money , (OD.Quantity * OD.UnitPrice)*(1-OD.Discount)) AS [LineTotal]
         FROM Orders AS O INNER JOIN Customers AS C        ON O.CustomerID = C.CustomerID
                          INNER JOIN [Order Details] AS OD ON O.OrderID    = OD.OrderID
                          INNER JOIN Products AS P         ON OD.ProductID = P.ProductID
         WHERE C.CustomerID = @CustomerID AND  O.OrderID = @OrderID 

         UNION ALL

        SELECT'-' AS CustomerID,'-' AS CompanyName,NULL AS OrderID,'' AS OrderDate,'-' AS ProductName,NULL AS Quantity , NULL AS UnitPrice,CONVERT(money , dbo.fn_GetOrderTotal(@CustomerID,@OrderID)) AS Total;

END
GO 

