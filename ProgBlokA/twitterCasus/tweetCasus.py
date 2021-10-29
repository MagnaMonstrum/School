import tweetDict

def userMsg():
  stationName = input('voer naam van het station in: ')
  msg = input('voer een bericht in: ')
  name = input('voer naam in: ')

  data =  f'{stationName}\n{name}\n'

  msgData = f'{msg}\n'

  if name == '':
      name = 'anoniem'

  newMsg = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'w')

  newMsg.write(msgData)
  newMsg.write(data)
  newMsg.close()


def moderate():
  msg = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'r')
  # userMsgLines = msg.readlines()
  msgString = msg.readline()
  print(msgString)
  # print(userMsgLines)
  msg.close()
  modVerdict = input('accept msg? ')

  if modVerdict == 'accept':
    msgAppend = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'a')
    msgAppend.write('Accepted')
    print('Accepted')
    msg.close()
    
  elif modVerdict == 'reject':
    msgAppend = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'a')
    msgAppend.write('Rejected')
    print('Rejected')
    msg.close()


userMsg()
moderate()
