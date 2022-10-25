class Contact(object):
    def __init__(self, name, pnum, mail, addr):
        self.name = name
        self.pnum = pnum
        self.mail = mail
        self.addr = addr

    def __str__(self):
        return f"{self.name}, {self.pnum}, {self.mail}, {self.addr}"

    @staticmethod
    def new_contact():
        name = input("이름: ")
        phone_number = input("전화번호: ")
        email = input("이메일: ")
        address = input("주소: ")
        return Contact(name, phone_number, email, address)