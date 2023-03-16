from requests import codes
good_codes = (codes.ok, codes.okay, codes.all_ok, codes.all_okay, codes.all_good, codes["\\o/"], codes["✓"])
print(good_codes)


my_tuple = (codes.ok, codes.okay, codes.all_ok)
my_tuple_size = len(my_tuple)
print(my_tuple_size)

from requests import codes
good_codes = (codes.ok, codes.okay, codes.all_ok, codes.all_okay, codes.all_good) + (codes["\\o/"], codes["✓"])
# ⚠️  Attention cependant, cela entraine la copie des tuples concaténés. Si vos tuples sont volumineux, cela peut être couteux.
print(good_codes)


from requests import codes
good_codes = (codes.ok, codes.okay, codes.all_ok, codes.all_okay, codes.all_good)
print(good_codes[4])


from requests import codes
good_codes = 100*(codes.ok, codes.okay)
print(good_codes)


# tuple_comprehension_result = (<expression> for <variable> in <iterable>)

