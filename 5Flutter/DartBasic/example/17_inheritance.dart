void main(){
  print('--------- idol ---------');
  Idol apink = Idol(name: 'apink', membersCount: 5);
  apink.sayName();
  apink.sayMembersCount();

  print('--------- boy group ---------');
  BoyGroup bts = BoyGroup('bts', 7);
  bts.sayName();
  bts.sayMembersCount();
  bts.sayMale();

  print('--------- girl group ---------');
  GirlGroup redvelvet = GirlGroup('redvelvet', 5);
  redvelvet.sayName();
  redvelvet.sayMembersCount();
  redvelvet.sayFemale();
}

class Idol{
  String name;
  int membersCount;

  Idol({
    required this.name,
    required this.membersCount,
  });

  void sayName(){
    print('${this.name}');
  }

  void sayMembersCount(){
    print('${this.membersCount}');
  }
}

class BoyGroup extends Idol{
  BoyGroup(
    String name,
    int membersCount,
  ): super(
      name: name,
      membersCount: membersCount,
  );
  
  void sayMale(){
    print('We are male.');
  }
}

class GirlGroup extends Idol{
  GirlGroup(
    String name,
    int membersCount,
  ): super(
      name: name,
      membersCount: membersCount,
  );
  
  void sayFemale(){
    print('We are female.');
  }
}