void main(){
  for(int i = 0; i < 10; i++){
    print(i);
  }

  List<int> numbers = [1,2,3,4,5,6];
  int total = 0;
  for(int j = 0; j < numbers.length; j++){
    total += numbers[j];
  }
  print(total);

  total = 0;
  for(int number in numbers){
    total += number;
  }
  print(total);

  total = 0;
  while(total<10){
    total += 1;
  }
  print(total);

  total = 0;
  do {
    total += 1;
  } while(total < 10);
  print(total);

  total = 0;
  while(total<10){
    total += 1;
    if(total == 5){
      break;
    }
  }
  print(total); //1,2,3,4,5

  total = 0;
  while(total<10){
    total += 1;
    if(total == 5){
      continue;
    }
  }
  print(total); //1,2,3,4,6,7,8,9,10
}