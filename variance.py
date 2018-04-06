from functools import reduce

def variance(data):
	mean = sum(data) / float(len(data))
	second_moment = sum([x*x for x in data]) / float(len(data))
	return (second_moment - mean*mean)

def function(data):
    ss, s, n = reduce(lambda a, b: map(sum, zip(a,b)), [(x*x, x, 1) for x in data])
    return (ss - s*s/n) / n

l1 = [x for x in range(1, 212)]
l2 = [-2*x*x + x - 2 for x in range(1, 212)]

# Sanity check
print("variance_mine_l1 = {0}".format(variance(l1)))
print("variance_org_l1 = {0}".format(function(l1)))
print("variance_mine_l2 = {0}".format(variance(l2)))
print("variance_org_l2 = {0}".format(function(l2)))