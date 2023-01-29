void main(){
  Idol blackPink = Idol(
    'black pink',
    ['Ji', 'Je', 'Li', 'Ro']
  );

  Idol bts = Idol.fromList(
    ['BTS', 
    ['RM', 'Jin', 'Sugar']]
  );

  print(blackPink.firstMember);
  print(bts.firstMember);
  
  bts.firstMember = 'Ironman';
  print(bts.firstMember);
}

class Idol{
  String name;
  List<String> members;

  Idol(this.name, this.members);
  
  Idol.fromList(List values)
  : this.name = values[0],
    this.members = values[1];

  void sayHello(){
    print('Hi, we are ${this.name}.');
  }

  void introduce(){
    print('our members are ${this.members}.');
  }

  String get firstMember{
    return this.members[0];
  }

  set firstMember(String name){
    this.members[0] = name;
  }
}