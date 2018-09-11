import os

while True:
  counter += 1
  answer = os.system('./shell.sh')

  if answer == 0:
    print('Success')
    os.rename('./show-run.log', './show-run_' + '{0:02d}'.format(counter) + '.log')
  else:
    print('Fail')
  if counter == 5:
    break
