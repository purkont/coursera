h_1 = int(input())
m_1 = int(input())
s_1 = int(input())
h_2 = int(input())
m_2 = int(input())
s_2 = int(input())
f_t = h_1 * 3600 + m_1 * 60 + s_1
s_t = h_2 * 3600 + m_2 * 60 + s_2
r_t = s_t - f_t
print(r_t)
