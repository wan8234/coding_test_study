import sys

input = sys.stdin.readline


N,K = map(int,input().split())

usage_list = list(map(int,input().split()))

m_tab = list()
m_count = 0
change = maximum = 0

while usage_list:

    next_use = usage_list[0]

    if len(m_tab) < 2:
        m_tab.append(next_use)
        usage_list.remove(next_use)

    elif next_use in m_tab:
        usage_list.remove(next_use)
        continue

    else:

        for i in range(len(m_tab)):

            if m_tab[i] not in usage_list:
                change = m_tab[i]
                break

            elif usage_list.index(m_tab[i]) > maximum:
                maximum = usage_list.index(m_tab[i])
                change = m_tab[i]

        m_tab[m_tab.index(change)] = next_use
        usage_list.remove(next_use)

        maximum = 0
        m_count += 1

print(m_count)
