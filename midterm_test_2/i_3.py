def sorted_with_weird_order(string_list, order):
	dic = {order[i]: i for i in range(len(order))}
	return sorted(string_list, key=lambda x: [dic[c] for c in x])

print(sorted_with_weird_order(['c', 'b', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
print(sorted_with_weird_order(['', 'ab', 'a'], 'abcdefghijklmnopqrstuvwxyz'))
print(sorted_with_weird_order(['c', 'b', 'a'], 'acbdefghijklmnopqrstuvwxyz'))
