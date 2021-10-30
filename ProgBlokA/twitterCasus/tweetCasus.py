from tweetDict import bericht

def userMsg():
  stationName = input('voer naam van het station in: ')
  msg = input('voer een bericht in: ')
  name = input('voer naam in: ')

  data =  f'{stationName}\n{name}\n'

  msgData = f'{msg}\n'

  if name == '':
      name = 'anoniem'

  newMsg = open("SchoolHU1/ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'w')
  tweet = open("SchoolHU1/ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'w')
  tweet.write(bericht)
  bericht.update({"inhoud":f"{msg}"})
  print(bericht)
  newMsg.write(msgData)
  newMsg.write(data)
  newMsg.close()


def moderate():
  msg = open("SchoolHU1/ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'r')
  # userMsgLines = msg.readlines()
  msgString = msg.readline()
  print(msgString)
  # print(userMsgLines)
  msg.close()
  modVerdict = input('accept msg? ')

  if modVerdict == 'accept':
    msgAppend = open("SchoolHU1/ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'a')
    msgAppend.write('Accepted')
    print('Accepted')
    msg.close()
    
  elif modVerdict == 'reject':
    msgAppend = open("SchoolHU1/ProgBlokA/twitterCasus/generated/tweetbericht.txt", 'a')
    msgAppend.write('Rejected')
    print('Rejected')
    msg.close()


userMsg()
moderate()
