--Total Sales
SELECT SUM(Sales) as Total_Sales
from Superstore;
--Total profit
Select sum(Profit) as Total_Profit
from Superstore;
--Sales by region
Select Region,sum(Sales) as SALES_BY_REGION 
from Superstore
group by Region
order by SALES_BY_REGION desc;
--Sales by category
Select Category,sum(Sales) as SALES_BY_CATEGORY
from Superstore
group by Category
order by SALES_BY_CATEGORY desc;
--Monthly Sales Trend
Select year(Order_Date) as Year,
month(Order_Date) as Month,
sum(Sales) as Total_Sales
from Superstore
group by Year,Month
order by Year,Month;
--Top 10 Products
Select Product_Name ,sum(Sales) as Total_Sales 
from Superstore
group by Product_Name
order by Total_Sales desc
limit 10;
--Most Profitable Category
Selecy Category , sum(Profit) as Total_Profit
from Superstore
group by Category
order by Total_Profit desc;
--Sales per year
Select year(Order_Date) as Year , sum(Sales) as Total_Sales
from Superstore
group by Year
order by Year;
--Avg order value
Select avg(Sales) as Avg_order_value
from Superstore;
--Loss making Products
Select Product_Name, Category ,Sales, sum(profit) as Total_profit
from Superstore
group by Product_Name,Category
having and Total_profit < 0;