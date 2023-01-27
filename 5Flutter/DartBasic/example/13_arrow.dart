void main(){
  int result = addNumbers(10, 20, 30);
  print('result: $result');
}

// arrow function
// 간소화 표현, => 뒤에 return을 바로 작성해줌.
int addNumbers(int x, int y, int z) => x+y+z;