name = input()
tickets_old_count = int(input())
tickets_young_count = int(input())
pure_cost_ticket_old = float(input())
cost_for_service = float(input())

pure_cost_ticket_young = pure_cost_ticket_old - (pure_cost_ticket_old * 0.7)
ticket_old_price = pure_cost_ticket_old + cost_for_service
ticket_young_price = pure_cost_ticket_young + cost_for_service
total_price = ticket_young_price * tickets_young_count + ticket_old_price * tickets_old_count

money = total_price * 0.2


print(f"The profit of your agency from {name} tickets is {money:.2f} lv.")