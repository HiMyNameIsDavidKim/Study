// 상태를 열거해 묶어서 정의한다.
enum Status{
  approved,
  pending,
  rejected,
}

void main(){
  Status status = Status.pending;

  if(status == Status.approved){
    print('approved.');
  }else if(status == Status.pending){
    print('pending.');
  }else{
    print('rejected.');
  }
}