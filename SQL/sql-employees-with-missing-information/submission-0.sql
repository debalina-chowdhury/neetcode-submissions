-- Write your query below
select e.employee_id
from employees e where employee_id not in
(select employee_id from salaries)
union all
select s.employee_id
from salaries s where employee_id not in
(select employee_id from employees)
order by employee_id