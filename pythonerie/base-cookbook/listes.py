from requests import codes
# good_codes = [codes.ok, codes.okay, codes.all_ok]

# from requests import codes
# good_codes = [codes.ok, codes.okay, codes.all_ok]
# my_list_size = len(good_codes)
# print(my_list_size)



# from requests import codes
# good_codes = [codes.ok, codes.okay, codes.all_ok, codes.all_okay, codes.all_good] + [codes["\\o/"], codes["✓"]]
# print(good_codes)


# from requests import codes
# good_codes = [codes.ok, codes.okay, codes.all_ok, codes.all_okay, codes.all_good]
# print(good_codes[4])



good_codes = [codes.ok, codes.okay, codes.all_ok, codes.all_okay, codes.all_good]
print(len(good_codes))
good_codes.append(codes["✓"])
print(len(good_codes))


good_codes.append(["I", "am", "a", "list"])
print(good_codes)



my_list = [1, "i’m in the list", [6.7, "i’m in a nested list !"]]


from requests import codes
good_codes = 100 * [codes.ok, codes.okay]
print(good_codes)


integers = [i for i in range(100)]
print(integers)