void main(){
  //Same as python's Dictionary. Key-Value structure.
  Map<String, String> dictionary = {
    'Harry': 'Potter',
    'Ron': 'Weasley',
    'Hermione': 'Granger'
  };
  print(dictionary);

  print(dictionary['Harry']);

  dictionary.addAll({
    'Spiderman': 'Peter'
  });
  print(dictionary);

  dictionary['Hulk'] = 'Brus';
  print(dictionary);

  dictionary.remove('Harry');
  print(dictionary);

  print(dictionary.keys);
  print(dictionary.values);
}