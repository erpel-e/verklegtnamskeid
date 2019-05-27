def get_data(aTuple):
    nums = ()
    words = ()
    for t in aTuple:
        nums = nums + (t[0],)
        if t[1] not in words:
            words = words + (t[1],)
    min_n = min(nums)
    max_n = max(nums)

    unique_words = len(words)
    return (min_n, max_n, unique_words)

tswift = ((2014, "harry"),(2014,"jake"),(2012, "harry"))
(min_year, max_year, num_people) = get_data(tswift)

print("from", min_year, "to", max_year, "taylors songs about", num_people)

perfect_square = (1,2,3,4,5)
print(len(perfect_square))

for p in perfect_square:
    print("p is:",p)
print(dir(perfect_square))