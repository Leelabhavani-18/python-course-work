data={
    'ajay':{'python':99,'mysql':88,'flask':90},
    'krishna':{'python':29,'mysql':100,'flask':50},
    'ruchitha':{'python':99,'mysql':98,'flask':96},
    'chintu':{'python':89,'mysql':85,'flask':70},
    'leela':{'python':45,'mysql':58,'flask':92},
    'praveen':{'python':30,'mysql':10,'flask':20}
    }
user=input("Enter the user: ")
avg= (data[user]['python']+data[user]['mysql']+data[user]['flask'])

if 80<=avg<=100:
      print(f'{user} got "A" grade.\nKeep it up')
elif 60<=avg<=80:
      print(f'{user} got "B" grade.\nGood. Need to improve')
elif 40<=avg<=60:
      print(f'{user} got "C" grade.\nAverage, Practice well for the next semester')
elif avg<40:
      print(f'{user} got "F" grade.\nFail,Bring your Parents')
      