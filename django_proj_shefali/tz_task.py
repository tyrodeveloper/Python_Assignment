import pandas as pd
import datetime
# from data_class import create
#df=pd.read_csv('eco_task.csv',sep='\t')
#print(df)
        
class task_list:


    def task_1(self,starttime, endtime):
        current_time=str(datetime.datetime.now())
        current_time=datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S.%f').time()
        start_time= datetime.datetime.strptime(starttime, '%H:%M:%S').time()
        end_time=datetime.datetime.strptime(endtime, '%H:%M:%S').time()
        # print(current_time,start_time,endtime)
        if start_time <= current_time and current_time <= end_time:
            return True
        elif start_time >= current_time:
            return start_time
        else:
            return False

    def enchanced_task(self,starttime, endtime, day):
        current_date= datetime.datetime.now()
        current_time=str(datetime.datetime.now())
        current_day=current_date.strftime('%A')
        current_day_int=datetime.datetime.today().weekday()
        current_time=datetime.datetime.strptime(current_time, '%Y-%m-%d %H:%M:%S.%f').time()
        days=list(day.split(' and '))
        days_all=["Monday","Tuesday","Wednesday","Thursday","Friday","Saturday","Sunday"]
        # days_int=[]
        for i in range(0,len(days)):
            idx=days_all.index(days[i])
            # days_int.append(idx)
            if idx==current_day_int and  self.task_1(self.starttime, self.endtime)==True:
                return True
            elif idx==current_day_int and self.task_1(self.starttime, self.endtime)==False:
                if i+1==len(days):
                    return days[0]+ ' ' + self.starttime
                else:
                    return days[i+1] + ' ' +self.starttime
            elif idx==current_day_int and str(self.task_1(self.starttime, self.endtime))==self.starttime:
                return days[i] + ' ' +self.starttime
                
            elif i==len(days)-1 and idx!=current_day_int:
                for k in range(0,len(days_all)):
                    if (days_all[k]==current_day):
                        if(k==len(days_all)-1):
                             for l in range(0,k):
                                    if days_all[l] in days:
                                        return days_all[l] + ' '+self.starttime
                        else:
                            for j in range(k+1,len(days_all)):
                                if days_all[j] in days:
                                    return days_all[j] + ' '+ self.starttime
                            else:
                                for l in range(0,k):
                                    if days_all[l] in days:
                                        return days_all[l] + ' '+self.starttime
                 

            



    def create(self,taskType,user,country,starttime,endtime,day=''):
            self.taskType=taskType
            self.user=user
            self.country=country
            self.endtime=endtime
            self.starttime=starttime
            self.day=day
            if(day==''):
                return self.task_1(self.starttime,self.endtime)
            else:
                return self.enchanced_task(self.starttime,self.endtime,self.day)


    # def create_enhanced_data(self,taskType,user,country,starttime,endtime,day):
    #         self.taskType=taskType
    #         self.user=user
    #         self.country=country
    #         self.endtime=endtime
    #         self.starttime=starttime
            
    #         return self.enchanced_task(self.starttime,self.endtime,self.day)








