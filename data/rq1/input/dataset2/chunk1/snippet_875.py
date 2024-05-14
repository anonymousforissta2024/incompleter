#Source: https://stackoverflow.com/questions/12946241/typeerrorenqueuqe-takes-1-positional-argument-but-2-were-passed
class Queue_demo:
    head=-1
    tail=-1
    a=[]

    def enqueue(data=10):
        if(head==-1 and tail==-1):
            head=head+1
            tail=tail+1
            a.append(data)
        else:
            tail=tail+1
            a.append(data)

    def dequeue():
        y=a[head]
        if(head==tail):
            head,tail=-1,-1
        else:
            head=head+1
        return y

q1=Queue_demo()
q2=Queue_demo()
q1.enqueue(12)

while(q1.tail==-1):
    print(q1.dequeue())