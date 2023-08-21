from dataclasses import dataclass

 

todo = []

 

 

@dataclass

class task:

    text: str

    isCompleted: bool = False

 

 

def add(title):

    title = title.replace('b', 'bbb').replace('B', 'Bbb')

    todo.append(task(title))

 

 

def get_all():

    return todo

 

 

def get(index):

    return todo[index]

 

 

def update(index):

    todo[index].isCompleted = not todo[index].isCompleted