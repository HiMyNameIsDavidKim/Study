void main(){
  //final and const can skip type declare.
  //build time : if we start run, 
  //             code will change to number. at that time.

  //final : not need to know 'build time'
  final name1 = 'code factory';
  print(name1);

  //const : need to know 'build time'
  const name2 = 'code factory';
  print(name2);
}