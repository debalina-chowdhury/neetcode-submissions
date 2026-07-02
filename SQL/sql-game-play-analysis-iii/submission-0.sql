-- Write your query below
select a1.player_id, a1.event_date,
sum(case when a1.player_id = a2.player_id and a1.event_date >= a2.event_date then a2.games_played else 0 end) as games_played_so_far
from activity a1
left join activity a2
on a1.player_id = a2.player_id
group by a1.player_id, a1.event_date
order by a1.player_id, a1.event_date