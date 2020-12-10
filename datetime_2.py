import datetime

current_weight = 220
goal_weight = 180
avg_weight_lost = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_weight_lost

print(end_date)
print(f'reaches my goal in {(end_date-start_date).days//7} weeks')