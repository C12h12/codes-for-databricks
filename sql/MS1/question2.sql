select c.customer_name,o.order_id,o.order_date,
(o.order_date - lag(o.order_date) over(partition by c.customer_name order by o.order_date)) as days_passed
from Orders o
join Customers c on c.customer_id=o.customer_id;
