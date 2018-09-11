import os
import time

counter = 0

while True:
  counter += 1
  answer = os.system('./shell.sh')

  if answer == 0:
    print('Success')
    os.rename('./show-run.log', './show-run_' + '{0:02d}'.format(counter) + '.log')
    now = time.ctime()
    cnvtime = time.strptime(now)
    print(time.strftime("%Y/%m/%d %H:%M", cnvtime))
  else:
    print('Fail')
  if counter == 5:
    break
