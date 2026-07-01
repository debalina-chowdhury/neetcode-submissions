-- Write your query below
select distinct title
from content c
left join tv_program tv
on c.content_id = tv.content_id
where kids_content = 'Y'
and content_type = 'Movies'
and program_date >= '2020-06-01'
and program_date < '2020-07-01'