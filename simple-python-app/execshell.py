import os
import datetime

counter = 0

while True:
  counter += 1
  answer = os.system('./shell.sh')

  if answer == 0:
    print('Success')
    os.rename('./show-run.log', './show-run_' + '{0:02d}'.format(counter) + '.log')
    date = datetime.datetime.today()
    time = str(date.strftime("%Y-%m-%d_%H:%M:%S"))
    print(time)
  else:
    print('Fail')
  if counter == 5:
    break
