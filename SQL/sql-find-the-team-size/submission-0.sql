-- Write your query below
select e.employee_id, t.team_size
from employee e
join
(select team_id, count(*) as team_size
from employee group by team_id) t
on e.team_id = t.team_id
order by e.employee_id