import pandas as pd
import random
import matplotlib.pyplot as plt

data = []

#utilize tesat on 20 assesors, and we visulize to record for each one to show their performance after trying the new version

for user in range(1,20):

    #old version

    data.append([
        user,
        "old",
        random.randint(6, 10), # steps_to_access_form --> user needed between 5–10 steps
        random.uniform(40, 90),  # time_to_open_form --> opening form took 40–90 seconds
        random.uniform(15, 30), # form_completion_time --> completing form took 15–30 minutes
        random.uniform(5, 20), # time_to_get_answer
        random.randint(2, 5), # communication_attempts --> multiple calls needed
        random.randint(0, 2), # missed_tasks --> sometimes missed tasks
        random.randint(2, 15) # schedule_delay
    ])

    data.append([
        user,
        "new",
        random.randint(3, 6), # steps_to_access_form --> user needed between 5–10 steps
        random.uniform(10, 30),  # time_to_open_form --> opening form took 40–90 seconds
        random.uniform(8, 18), # form_completion_time --> completing form took 15–30 minutes
        random.uniform(2, 10), # time_to_get_answer
        random.randint(1, 2), # communication_attempts --> multiple calls needed
        random.randint(0, 1), # missed_tasks --> sometimes missed tasks
        random.randint(0, 10) # schedule_delay
    ])

columns = [
    "user_id", "version",
    "steps_to_access_form",
    "time_to_open_form",
    "form_completion_time",
    "time_to_get_answer",
    "communication_attempts",
    "missed_tasks",
    "schedule_delay"
]

df = pd.DataFrame(data, columns = columns )
grouped = df.groupby('version').mean()


#comparison of average steps to access form
grouped['steps_to_access_form'].plot(kind = 'bar', title = 'Average Steps to Access Form', xlabel = 'Version',
ylabel = 'Number of Steps', color = 'yellow')
plt.show()

# comparison of form completion time
grouped['form_completion_time'].plot(kind = 'bar', title = 'Average Form Completion Time', xlabel = 'Version',
ylabel = 'Time (minutes)', color = 'purple')
plt.show()

# comparison of communication attempts needed
grouped['communication_attempts'].plot(kind = 'bar', title = 'Communication Attempts Needed', xlabel = 'Version', 
ylabel = 'Attempts', color = 'pink')
plt.show()

# comparison of Time to Receive Support
grouped['time_to_get_answer'].plot(kind = 'bar', title = 'Time to Receive Support', xlabel = 'Version',
ylabel = 'Time (minutes)', color = 'green')
plt.show()