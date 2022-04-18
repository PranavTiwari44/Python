# jabber = open("Jabberwocky.txt", 'r')
#
# for line in jabber:
#     print(line, end='')
#
# jabber.close()

with open("Jabberwocky.txt", "r") as jabber:
    #  for line in jabber:
    #     print(line.strip())
    # print()
    lines = jabber.readlines()
    print(lines)
