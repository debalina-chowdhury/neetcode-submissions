-- Write your query below
select a.player_id, a.device_id
from activity a
join
(select player_id, min(event_date) first_login
from activity group by player_id) e
on a.event_date = e.first_login and a.player_id = e.player_id
order by a.player_id