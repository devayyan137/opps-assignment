class student:
    def __init__(self,sub1,sub2,sub3):
        self.sub1=sub1
        self.sub2=sub2
        self.sub3=sub3
        sum= sub1+sub2+sub3
        avg=sum/3
        print(avg)
sub1=student(65,73,83)