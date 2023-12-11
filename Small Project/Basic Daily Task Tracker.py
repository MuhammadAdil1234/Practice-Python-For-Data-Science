#!/usr/bin/env python
# coding: utf-8

# In[ ]:


from datetime import datetime, time

class DailyTask:
    tasks = {'task': [], 'starttime': [], 'endtime': []}

    def __init__(self, task_name, start_time, end_time):
        self.task_name = task_name
        self.start_time = time(int(start_time), 0, 0)
        self.end_time = time(int(end_time), 0, 0)

    def organize_task(self):
        self.tasks['task'].append(self.task_name)
        self.tasks['starttime'].append(self.start_time)
        self.tasks['endtime'].append(self.end_time)
        return self.tasks

    def manage_task(self):
        print('Task             Start Time              End Time               Status')
        print('-------------------------------------------------------------------------')
        length = len(self.tasks['task'])
        current_time = datetime.now().time()
        for i in range(length):
            if current_time < self.tasks['endtime'][i]:
                st = 'Incomplete'
            else:
                st = 'completed'
            print('{}             {}              {}              {}'.format(
                self.tasks['task'][i], self.tasks['starttime'][i], self.tasks['endtime'][i], st))

    def delete_task(self):
        task_name = input('Enter The Task Name to Delete: ')

        # Create a reversed copy of the list for iteration
        reversed_indices = reversed(range(len(self.tasks['task'])))

        for i in reversed_indices:
            if task_name == self.tasks['task'][i]:
                self.tasks['task'].pop(i)
                self.tasks['starttime'].pop(i)
                self.tasks['endtime'].pop(i)

x = True
while x:
    print('----------Daily Task Tracker------------')
    print('----------------------------------------')
    print('---------Press 1 to enter Task----------')
    print('---------Press 2 to show Detail---------')
    print('---------Press 3 to delete Task---------')
    print('---------Press 4 to exit program--------')
    print('----------------------------------------')
    enter = input('Press Something?: ')

    if enter == '1':
        count = input('How many tasks do you want to add?: ')
        for c in range(int(count)):
            t_name = input('Please enter Your Task Name?: ')
            s_time = input('Please enter Start Time?: ')
            e_time = input('Please enter End Time?: ')
            obj = DailyTask(t_name, s_time, e_time)
            obj.organize_task()
    elif enter == '2':
        obj.manage_task()
    elif enter == '3':
        obj.delete_task()
        obj.manage_task()
    elif enter == '4':
        x = False


# In[ ]:





# In[5]:





# In[ ]:




