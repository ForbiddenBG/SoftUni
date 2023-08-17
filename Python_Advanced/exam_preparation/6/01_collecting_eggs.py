from collections import deque

eggs_sizes = deque([int(x) for x in input().split(", ")])
papers_sizes = deque([int(x) for x in input().split(", ")])

BOX_SIZE = 50
box_counter = 0

while eggs_sizes and papers_sizes:
    first_egg = eggs_sizes.popleft()
    if first_egg <= 0:
        continue
    if first_egg == 13:
        first_paper = papers_sizes.popleft()
        last_paper = papers_sizes.pop()
        papers_sizes.append(first_paper)
        papers_sizes.appendleft(last_paper)
        continue
    last_paper = papers_sizes.pop()
    if first_egg + last_paper <= BOX_SIZE:
        box_counter += 1

if box_counter > 0:
    print(f'Great! You filled {box_counter} boxes.')
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs_sizes:
    print(f"Eggs left: {', '.join([str(x) for x in eggs_sizes])}")
if papers_sizes:
    print(f"Pieces of paper left: {', '.join([str(x) for x in papers_sizes])}")
