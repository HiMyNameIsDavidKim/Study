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