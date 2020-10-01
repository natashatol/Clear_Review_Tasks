#install and load sql settings for jupyter notebook
%%! pip install -- trusted-host pypi.org ipython-sql
%load_ext sql

#connect to sql server
%sql sqlite://

#import pandas to retrieve excel file, creating a data frame from the Analyst Table
import pandas as pd
df = pd.ExcelFile(r'/Users/tashtol/Desktop/Analyst_Test.xlsx')
print(df)

#creating the table
table = pd.read_excel(r'/Users/tashtol/Desktop/Analyst_Test.xlsx')
table.head()

#work out the number of conversations had by each individual manager, ordered by the total number of conversations
%%sql
select managerid, count(conversationid) as number_of_conversation
from table
group by managerid
order by number_of_conversations

#work out the number of each type of conversation ocurring,
select conversationtype, count(conversationtype) as number_of_conversations
from table
order by number_of_conversations

