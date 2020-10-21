Task Execution Based on time Zone

Here we are creating some task. task can be created any time but should be executed only during the time range specified.

there was 2 type of task creation and execution 

part1: it's a simple task execution based on time. Whenever i'll create a task it'll check the current time  and task time range  so there will be 3 condition:
1. current time is between time range of task then we can execute this task and it will return true:

2. if current time is less than the start time  it will give you the start time of the task 

3. if current time is greter then end time it'll give you Faslse because there is no next time slot for current day.

But in this case we are not considering any day because if time  slot is not present on that day we can give the next time slot for next day when task can be executed for that we are doing some enhancement in task execution.

Enhanced Version:

Here we also specidy day of the task execution. there will be different scenarios as follows:

1. if current day we can execute this task so i need to check current  time if current time is between start time and end time. it'll give you true because current day and time is matching so we can execute thi task immediatly.

2. what if current day is matching but current time is less than start time then it'll retun current day and start time of the task

3. what if current day is matching but current time is greater than end time then we can search for next time and next day and then return next day when we can execute thi task and return start time

4. what if current day is not matching then current time matching will not impact our result because any how we need to select next day when we can execute this task and next day start time 

Directory Structure:

Project _name= PYthon_Proj

pkg_name=django_proj_shefali

django_proj_shefali
---__init.py
---tz_task.py

tz_task.py : in this file i have created all the variable and methods in a task_list class and import datetime and pandas libraries to get the current weekday and current time.


test.py : here i am creating all the test cases for all the scenarios and also put the comment before the test case so that u can identify each test case scenario and when i was doing the testing my current time is between 11:00 to 11:30 and day is Sunday so if you want all the test case in successfull condition. you need to modify test cases.

to run the code
1. cd Python_proj
2. python test.py


NOTE: i have also created the package for the name but i am not able to deploy due to some credential issue

