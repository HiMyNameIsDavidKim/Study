void main(){
  Idol blackPink = Idol(
    'black pink',
    ['Ji', 'Je', 'Li', 'Ro']
  );

  print(blackPink.name);
  print(blackPink.members);
  blackPink.sayHello();
  blackPink.introduce();

  Idol bts = Idol.fromList(
    ['BTS', 
    ['RM', 'Jin', 'Sugar']]);

  print(bts.name);
  print(bts.members);
  bts.sayHello();
  bts.introduce();
}

class Idol{
  final String name;
  final List<String> members;

  const Idol(this.name, this.members);
  
  Idol.fromList(List values)
  : this.name = values[0],
    this.members = values[1];

  void sayHello(){
    print('Hi, we are ${this.name}.');
  }

  void introduce(){
    print('our members are ${this.members}.');
  }
}