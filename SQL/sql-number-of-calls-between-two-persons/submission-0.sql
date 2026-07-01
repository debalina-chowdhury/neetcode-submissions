-- Write your query below
select person1, person2, 
count(*) as call_count, 
sum(duration) as total_duration
from
(select least(from_id, to_id) as person1, 
greatest(from_id, to_id) as person2, 
duration
from calls) order_calls
group by person1, person2