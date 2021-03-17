from collections import Counter
texts = [ "dum", "gum","dog"]
strGiven = "god"
print("Original list of strings:")
print(texts)
result = list(filter(lambda x: (Counter(strGiven) == Counter(x)), texts))
print("\nAnagrams of 'god' in the above string: ")
print(result)
