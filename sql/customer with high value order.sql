select o.order_id,c.name as customer_name,o.total_amount
from Orders o
join Customers c on c.customer_id=o.customer_id
where o.total_amount=(select max(total_amount) from Orders);

select max(total_amount) from Orders;
