import unittest
from django_proj_shefali import tz_task

class TestSum(unittest.TestCase):

    # My Current Time i 11:00 to 11:30 and My current date is Sunday Based on that i am creating test cases

 #  task cant not be executed immediately but there is a next time   
    def test_case_1(self):
        t2=tz_task.task_list()
        result=t2.create('CALL', 'U2' ,'India', '13:00:00', '14:30:00')
        print(result)
        # self.assertEqual(str(result), '13:00:00',"TESTED SUCCESSFULLY")

# task should be executed immediately
    def test_case_2(self):
        t2=tz_task.task_list()
        result=t2.create('CALL', 'U2' ,'India', '10:00:00', '12:30:00')
        print(result)
        # self.assertEqual(result, True,"TESTED SUCCESSFULLY")

# task cant be executed immediately and there is no next time
    def test_case_3(self):
        t2=tz_task.task_list()
        result=t2.create('CALL', 'U2' ,'India', '8:00:00', '10:30:00')
        print(result)
        # self.assertEqual(result, False,"TESTED SUCCESSFULLY")

# for enhanced version
#  if day is matching  and  task cant execute immediately but there is next time slot available 
    def test_case_4(self):
        t2=tz_task.task_list()
        result=t2.create('Email','U1','India','12:30:00','15:00:00','Saturday and Sunday')
        print(result)
        # self.assertEqual(result, 'Sunday 12:30:00',"TESTED SUCCESSFULLY")

# if day is matching and task can be executed immediately
    def test_case_5(self):
        t2=tz_task.task_list()
        result=t2.create('Email','U1','India','10:30:00','13:00:00','Tuesday and Sunday')
        print(result)
        # self.assertEqual(result, True,"TESTED SUCCESSFULLY")

# if day is matching and task cant executed immediately and there is no next time slot for the current day
    def test_case_6(self):
        t2=tz_task.task_list()
        result=t2.create('Email','U1','India','8:30:00','10:30:00','Tuesday and Sunday')
        print(result)
        # self.assertEqual(result, 'Tuesday 8:30:00',"TESTED SUCCESSFULLY")


### if day is not matching  so there is no effect if current time is between the interwal or before and after the interval 
# we have to take the start time for the next day for all the test cases
    
    def test_case_7(self):
        t2=tz_task.task_list()
        result=t2.create('Email','U1','India','8:30:00','10:30:00','Tuesday and Thursday')
        print(result)
        # self.assertEqual(result, 'Tuesday 8:30:00',"TESTED SUCCESSFULLY")

    def test_case_8(self):
        t2=tz_task.task_list()
        result=t2.create('Email','U1','India','12:30:00','15:00:00','Tuesday and Thursday')
        print(result)
        # self.assertEqual(result, 'Tuesday 12:30:00',"TESTED SUCCESSFULLY")

    def test_case_9(self):
        t2=tz_task.task_list()
        result=t2.create('Email','U1','India','10:30:00','13:00:00','Tuesday and Thursday')
        print(result)
        # self.assertEqual(result, 'Tuesday 10:30:00',"TESTED SUCCESSFULLY")

    


    

    # def test_case_2(self):
    #     self.assertEqual(sum((1, 2, 2)), 6, "Should be 6")

if __name__ == '__main__':
    unittest.main()



