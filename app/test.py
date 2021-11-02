l1=['1','2','3','4','5']
array_1=['0',9,'2']
# l3=l1+l2
# l3=l3
# print(sorted(l3))
# x=[sorted(i) for i in l3]
# print(x)
new=[int(item) for item in array_1]
print("new", new)

sentence ="love great awesome words I"
print(sentence.split(" "))
def sort_by_length(sentence):
    i = 1
    array = sentence.split(" ")
    while i < len(array):
        to_insert = array[i]
        j = i
        # Search in the sorted portion of the array
        # for the correct position to insert array[i]
        while j > 0 and len(array[j-1]) > len(to_insert):
            array[j] = array[j-1]
            j -= 1
        array[j] = to_insert
        i += 1
    print(array)

sort_by_length(sentence)