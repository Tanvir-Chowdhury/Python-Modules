import datetime
import calendar

'''current_weight = 220
goal_weight = 180
avg_weight_lost = 1.5

start_date = datetime.date.today()
end_date = start_date

while current_weight > goal_weight:
    end_date += datetime.timedelta(days=7)
    current_weight -= avg_weight_lost

print(end_date)
print(f'reaches my goal in {(end_date-start_date).days//7} weeks')'''

balance = 5000
interest_rate = 0.13
monthly_payment = 500

today = datetime.date.today()
days_in_current_month = calendar.monthrange(today.year, today.month)[1]
days_till_end_month = days_in_current_month - today.day

start_date = today + datetime.timedelta(days=days_till_end_month+1)
end_date = start_date

while balance <0 :
    interest_charge = (interest_rate / 12) * balance
    balance -= monthly_payment
    balance += interest_charge

    balance = round(balance, 2)
    if balance <  0:
        balance = 0

    print(end_date, balance)

    days_in_current_month = calendar.monthrange(end_date.year, end_date.month)[1]
    end_date = end_date + datetime.timedelta(days=days_till_end_month+1)