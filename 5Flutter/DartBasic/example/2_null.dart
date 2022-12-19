void main(){
  //when you want to change to null type,
  //add '?' after type.
  String? name1 = 'code factory';
  print(name1);
  name1 = null;

  //when you want explain this is not null,
  //add '!' after var.
  String? name2 = 'code factory';
  name2 = null;
  print(name2!);
}