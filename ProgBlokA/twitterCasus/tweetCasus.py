def userMsg():
  stationName = input('voer naam van het station in: ')
  msg = input('voer een bericht in: ')
  name = input('voer naam in: ')

  data =  '{}\n{}\n{}\n'.format(stationName, msg, name)

  if name == '':
      name = 'anoniem'

  newMsg = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'w')

  newMsg.write(data)
  newMsg.close()


def moderate():
  msg = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'r')
  userMsgLines = msg.readlines()
  print(userMsgLines)
  modVerdict = input('accept msg? ')

  if modVerdict == 'accept':
    msgAppend = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'a')
    msgAppend.write('Accepted')
    print('Accepted')
    
  elif modVerdict == 'reject':
    msgAppend = open("ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'a')
    msgAppend.write('Rejected')
    print('Rejected')



userMsg()
moderate()
