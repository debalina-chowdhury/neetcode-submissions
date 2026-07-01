-- Write your query below
select name,
sum(amount) as balance
from users
left join transactions
on users.account = transactions.account
group by name
having sum(amount) > 10000