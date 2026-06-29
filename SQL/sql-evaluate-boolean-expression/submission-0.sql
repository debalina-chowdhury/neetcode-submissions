-- Write your query below
select e.*,
case when e.operator = '>' and lv.value <= rv.value then False
when e.operator = '<' and lv.value >= rv.value then False
when e.operator = '=' and 
(lv.value < rv.value or lv.value > rv.value) 
then False else True end as value
from expressions e
left join variables lv
on e.left_operand = lv.name
left join variables rv
on e.right_operand = rv.name