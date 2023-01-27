void main(){
  Operation operation = add;
  int result = operation(10, 20, 30);
  print(result);

  operation = sub;
  result = operation(10, 20, 30);
  print(result);

  result = cal(10, 20, 30, add);
  print(result);

  result = cal(10, 20, 30, sub);
  print(result);
}

//typedef라는 곳에 여러 종류의 함수를 담을 수 있다.
typedef Operation = int Function(int x, int y, int z);

int add(int x, int y, int z) => x + y + z;
int sub(int x, int y, int z) => x - y - z;

//실제 사용 시 파이썬의 람다와 유사하게 사용.
int cal(int x, int y, int z, Operation operation){
  return operation(x, y, z);
}