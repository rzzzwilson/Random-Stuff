def dictionary_count(string):

  words = string.lower().split()
  my_dict = {}

  # for each word in the string
  for word in words:
      #my_dict[word] = my_dict.get(word, 0) + 1
      my_dict[word] = my_dict[word] + 1

  return my_dict

d = dictionary_count("I am a happy coder and I am learning Python")
print(d)
