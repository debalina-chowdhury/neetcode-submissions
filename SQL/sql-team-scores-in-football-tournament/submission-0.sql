with points as (
    select match_id, host_team as team_id,
        case when host_goals > guest_goals then 3
             when host_goals = guest_goals then 1
             else 0 end as goals
    from matches
    union all
    select match_id, guest_team as team_id,
        case when guest_goals > host_goals then 3
             when guest_goals = host_goals then 1
             else 0 end as goals
    from matches
)
select t.team_id, t.team_name,
       coalesce(ht.num_points, 0) as num_points        -- <-- COALESCE HERE, after the join
from teams t
left join (
    select team_id, sum(goals) as num_points
    from points
    group by team_id
) ht on t.team_id = ht.team_id
order by num_points desc, t.team_id;