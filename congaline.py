from sys import stdin, stdout
n,couples=map(int,input().split())
class Node:
    def __init__(self, data):
        self.data = data
        self.partner=None
        self.prev = None
        self.next = None
class DoublyLinkedList:
    def __init__(self):
        self.head=None
        self.tail=None
    def append(self, data,i):
        new_node = Node(data)
        if self.head is None:
            self.head=new_node
            self.tail=new_node
            self.head.next=None
            self.tail.next=None
            
        else:
            temp_tail=self.tail
            temp_tail.next=new_node
            new_node.prev=temp_tail
            self.tail=new_node
            if i%2 != 0:
                self.tail.prev.partner = self.tail
                self.tail.partner=self.tail.prev
    def display(self):
        current = self.head
        while current:
            stdout.write(current.data)
            stdout.write('\n')
            current = current.next
dllist = DoublyLinkedList()
dic={}
lst=[]
instructions=''
line = stdin.readline()
while line:
    if len(line.split())==2:
        couple1,couple2=line.split()[0],line.split()[1]
        lst+=[couple1,couple2]
    elif len(line.split())==1:
        instructions=line.split()[0]
    line = stdin.readline()
for i in range(len(lst)):
    dllist.append(lst[i],i)

current_person=dllist.head
permanent_head=dllist.head
current_tail= dllist.tail
if len(instructions)!=0:
    for instruction in instructions:
        if instruction=='P':
            stdout.write(current_person.partner.data)
            stdout.write('\n')
        elif instruction=='B':
            current_person=current_person.next
            #print('B operation current person now is '+current_person.data)
        elif instruction=='F':
            current_person=current_person.prev
            #print('F operation current person now is '+current_person.data)
        elif instruction=='R':
            person_to_remove=current_person
            if person_to_remove.next==None:  #If person to be removed is at end of queue, change current person = head of list
                #print('person to remove was at end of R operation'+person_to_remove.data)
                current_person=dllist.head
                #print('current Person now is R operation ' + current_person.data)
            else:
                if person_to_remove==dllist.head: #If person to be removed is at the head
                    dllist.head=person_to_remove.next #change head to next person
                    current_person=dllist.head #Curr person also points to new head
                    #print('R operation current person now is '+current_person.data)
                    person_to_remove.prev=None 
                    person_to_remove.next=None
                    person_to_remove.prev = current_tail
                    current_tail.next = person_to_remove
                    current_tail = person_to_remove
                else:
                    current_person=current_person.next
                    #print('R operation current person now is '+current_person.data)
                    person_to_remove.prev.next=person_to_remove.next
                    person_to_remove.next.prev=person_to_remove.prev
                    person_to_remove.prev=None
                    person_to_remove.next=None
                    person_to_remove.prev = current_tail
                    current_tail.next = person_to_remove
                    current_tail = person_to_remove
            #print('R operation')
            #dllist.display()
        else:
            person_to_remove=current_person
            if person_to_remove.next==None:
                current_person=dllist.head #Move to front
                if person_to_remove.partner!=person_to_remove.prev:
                    person_to_remove.prev.next=None
                    current_tail=person_to_remove.prev #updating tail
                    #print('tail now is '+current_tail.data)
                    person_to_remove.next=None
                    person_to_remove.prev=None
                    person_to_remove.next=person_to_remove.partner.next
                    person_to_remove.partner.next.prev=person_to_remove
                    person_to_remove.partner.next=person_to_remove
                    person_to_remove.prev=person_to_remove.partner
            else:
                #print('Person to remove not at end '+person_to_remove.data)
                if person_to_remove==dllist.head:
                    #print('Yay')
                    dllist.head=person_to_remove.next
                    current_person=dllist.head
                    person_to_remove.next=None
                    person_to_remove.prev=None
                    if person_to_remove.partner.next==None:
                        person_to_remove.partner.next=person_to_remove
                        person_to_remove.prev=person_to_remove.partner
                        current_tail=person_to_remove
                        person_to_remove.next=None
                    else:
                        person_to_remove.next=person_to_remove.partner.next
                        person_to_remove.partner.next.prev=person_to_remove
                        person_to_remove.partner.next=person_to_remove
                        person_to_remove.prev=person_to_remove.partner
                else:
                    current_person=person_to_remove.next
                    person_to_remove.prev.next=person_to_remove.next
                    person_to_remove.next.prev=person_to_remove.prev
                    person_to_remove.next=None
                    person_to_remove.prev=None
                    if person_to_remove.partner.next==None:
                        person_to_remove.partner.next=person_to_remove
                        person_to_remove.prev=person_to_remove.partner
                        current_tail=person_to_remove
                        person_to_remove.next=None
                    else:
                        person_to_remove.next=person_to_remove.partner.next
                        person_to_remove.partner.next.prev=person_to_remove
                        person_to_remove.partner.next=person_to_remove
                        person_to_remove.prev=person_to_remove.partner
                        
            #print('C operation')
            #dllist.display()
                
            
            
stdout.write('\n')
dllist.display()

