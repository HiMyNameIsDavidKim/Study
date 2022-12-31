void main(){
  int result = addNumbers(10, 20, 30);
  print('result: $result');
  int result2 = addNumbers2(z: 30, y: 20, x: 10);
  print('result2: $result2');
}

int addNumbers(int x, int y, int z){
  int sum = x + y + z;
  print('$x + $y + $z = $sum');

  if(sum%2 == 0){
    print('evn number');
  } else{
    print('odd number');
  }

  return sum;
}

int addNumbers2({
  required int x, 
  required int y, 
  required int z,
  }){
  int sum = x + y + z;
  print('$x + $y + $z = $sum');

  if(sum%2 == 0){
    print('evn number');
  } else{
    print('odd number');
  }
  return sum;
}