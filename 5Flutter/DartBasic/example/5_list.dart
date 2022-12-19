void main(){
  List<String> codeF = ['F', 'a', 'c', 't', 'o', 'r', 'y'];
  print(codeF);

  print(codeF[0]);
  print(codeF[1]);
  print(codeF[2]);
  print(codeF[3]);

  print(codeF.length);

  codeF.add('+');
  print(codeF);
  codeF.remove('+');
  print(codeF);
  print(codeF.indexOf('F'));
}