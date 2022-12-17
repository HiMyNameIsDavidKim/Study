void main(){
  int num1 = 2;
  print(num1 + 2);
  print(num1);

  //plus 1 and save.
  num1 ++;
  print(num1);

  //plus x and save.
  num1 += 2;
  print(num1);

  //NVL option. (if null change to this.)
  double? num2 = 4.0;
  print(num2);
  num2 = null;
  print(num2);
  num2 ??= 3.0;
  print(num2);

  //type judge.
  int num3 = 1;
  print(num3 is int);
  print(num3 is String);
  print(num3 is! int);
  print(num3 is! String);
}