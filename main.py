from set_stack import set_stack

s = set_stack()
print(s.check_for_shown_set())
for c in s.shown:
    print(c)
i_1 = int(input())
i_2 = int(input())
i_3 = int(input())
if s.check_selected_cards(i_1, i_2, i_3):
    print("FOUND")
for c in s.shown:
    print(c)

