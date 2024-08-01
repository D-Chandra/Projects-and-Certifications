class RatingOutofRangeError(Exception):
    def __init__(self,msg="Rating Out of range"):
        self.msg = msg
        super().__init__(self.msg)
check = 1
while check:
    try:
        print("Enter The Rating of 3 participants one by one::")
        Cons1 = int(input("Enter Rating For Participant1::"))
        if(Cons1<0 or Cons1>10):
            raise RatingOutofRangeError
        Cons2 = int(input("Enter Rating For Participant2::"))
        if(Cons2<0 or Cons2>10):
            raise RatingOutofRangeError
        Cons3 = int(input("Enter Rating For Participant3::"))
        if(Cons3<0 or Cons3>10):
            raise RatingOutofRangeError
        # winner = max(Cons1,Cons2,Cons3)
        # print("The Winner of is::",winner)
        if(Cons1>Cons2 and Cons1>Cons3):
            print("The Winner of is::Participant1")
        elif(Cons2>Cons1 and Cons2>Cons3):
            print("The Winner of is::Participant2")
        elif(Cons3>Cons1 and Cons3>Cons2):
            print("The Winner of is::Participant3")
        elif(Cons1 == Cons2):
            if(Cons2 == Cons3):
                print("Tie Between all 3")
            print("Tie Between Participant1 and Participant2")
        
        else:
            print("Tie Between 3")

    except RatingOutofRangeError as n:
        print(n)
    finally:
        print("Enter 1 to Continue or 0 to exit")
        check = int(input("Enter Value::"))