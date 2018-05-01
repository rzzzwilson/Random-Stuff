def dictionary_count(string):

  words = string.lower().split()
  my_dict = {}

  # for each word in the string
  for word in words:
      str_occurences = string.count[word[:len(string)]]
      my_dict[word] = str_occurences

      removal_counter = str_occurences

    # remove each instance of the word in `words_in_string` to avoid duplicate keys
      while removal_counter > 0:
          words.remove(word)
          removal_counter -= 1


  return my_dict

dictionary_count("I am a happy coder and I am learning Python")
