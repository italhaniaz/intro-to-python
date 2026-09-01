import os
from time import sleep
from datetime import datetime
from collections import defaultdict


class ToDoList:
    def __init__(self):
        self.d = defaultdict(list)

    def add_task(self, priority, task):
        self.d[priority].append(task)

    def show_tasks(self):
        print('-----------------')
        print('Priority - Tasks ')
        print('-----------------')
        for k, v in self.d.items():
            print(f'   {k}\t  {v}')

    def remove_task(self, priority):
        if self.d[priority]:
            self.d[priority].pop(0)
        else:
            print("Nothing")

    def save_to_file(self):
        directory = 'tasks'
        if not os.path.exists(directory):
            os.mkdir(directory)

        # this is the file name which is current dd-mm-yyyy
        name = datetime.today().strftime('%d-%m-%Y')

        out_filename = os.path.join(directory, name)

        with open(out_filename, 'a') as f:
            for k, v in self.d.items():
                task = str(k) + '\t' + str(v)
                f.write(task+'\n')
            
        print("file saved")
        sleep(2)


def to_do_menu():
    print("--------------")
    print("  TO-DO-LIST  ")
    print("--------------")
    print("[1] ADD TASK   [2] REMOVE TASK \n[3] SHOW TASKS [4] SAVE TO FILE\n[5] EXIT")
    print("--------------")


def to_do_list():
    l = ToDoList()
    while True:
        to_do_menu()
        option = int(input("Enter your choice: "))
        is_int = isinstance(option, int) 

        if not is_int:
            raise TypeError("Given datatype is incorrect")

        if option == 1:
            priority = int(input("Enter task priority e.g 1, 2... : "))

            is_int = isinstance(priority, int) 
            if not is_int:
                 raise TypeError("Given datatype is incorrect")

            task = input("Enter task: ")
            l.add_task(priority, task)

        if option == 2:
            priority = int(input("Enter task priority to remove: "))
            l.remove_task(priority)

        if option == 3:
            l.show_tasks()
            sleep(5)

        if option == 4:
            l.save_to_file()
        
        if option == 5:
            print("Exiting .... ")
            sleep(2)
            print("Thanks for using ^_^")
            break


if __name__ == "__main__":
    to_do_list()