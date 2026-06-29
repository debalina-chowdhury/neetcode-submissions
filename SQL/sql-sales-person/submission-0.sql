-- Write your query below
select s.name from sales_person s
where sales_id not in
(select sales_id from orders o
left join company c
on o.com_id = c.com_id
where c.name = 'CRIMSON')
ORDER BY s.name
