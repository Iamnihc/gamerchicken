import seaBattle
import wikipedia
import discord
import c4
p1 = None
p2 = None

gamemessage = None
game = seaBattle.fullgame(10,1)
client = discord.Client()

import requests
import re
import random
import collections
fscore = 0
comicdata = []
dp = 0

# Set the URL you want to webscrape from
url = 'https://xkcd.com/archive/'

# Connect to the URL
response = requests.get(url)

# Parse HTML and save to BeautifulSoup objectÂ¶

tags =  response.text.split('(Hover mouse over title to view publication date)<br /><br />')[1]

tags = tags.split('</div>')[0]
tags = tags.split('<br/>')[:-1]


for i in tags:
    comicname = re.search(">[\S\w\s]*<",i)[0][1:-1].lower()
    comicnum =  re.search("/\d*/", i )[0][1:-1].lower()
    comicdata.append([comicname,comicnum])
comicdata.reverse()
@client.event

async def on_ready():
    print('We have logged in as {0.user}'.format(client))

@client.event
async def on_message(message):
    global p1, p2, shipon, p1dm, p2dm, game, board1m, board2m, comicdata, boardm, player, board, dp, fscore, turnm
    print(message.content)
    if message.author == client.user:
        return
    if message.content.startswith("$w"):
        x = (wikipedia.search(message.content[3:]))
        page = wikipedia.page(x[0])
        sentance = (page.summary.split(".")[0])
        img = page.images[0]
        await message.channel.send(sentance + "\n Here is a picture: " + img)
        await message.channel.send("Read more at: <"  + page.url + ">")
    # if ("sorr" in message.content.lower() or "sry" in message.content.lower()  )and message.author.id == 598769660866854913 :
    #     await message.channel.send("why are u apologizing")
    if str(message.content).lower() == "hi":
        fscore +=1
        await message.channel.send("hi. Your politeness score with this bot has been increased to " + str(fscore))
    # if "frick" in str(message.content).lower():
    #     fscore -=1
    #     await message.channel.send("wow rude. ur politeness score is " + str(fscore))
    # if "fuck" in str(message.content).lower():
    #     fscore -=1
    #     await message.channel.send("wow rude. ur politeness score is " + str(fscore))
    # if "heck" in str(message.content).lower():
    #     fscore -=1
    #     await message.channel.send("wow rude. ur politeness score is " + str(fscore))
    # if "hell" in str(message.content).lower() and not "hello" in str(message.content).lower():
    #     fscore -=1
    #     await message.channel.send("wow rude. ur politeness score is " + str(fscore))
    # if "shit" in str(message.content).lower():
    #     fscore -=1
    #     await message.channel.send("wow rude. ur politeness score is " + str(fscore))
    # if "shoot" in str(message.content).lower():
    #     fscore -=1
    #     await message.channel.send("wow rude. ur politeness score is " + str(fscore))
    if ":((" in str(message.content).lower():
        await message.channel.send("why does he have " + str(str(message.content).lower().count("(")) + " mouths. Big sad.")
    if ":))" in str(message.content).lower():
        await message.channel.send("why does he have " + str(str(message.content).lower().count(")")) + " mouths? at least hes happy.")


    if message.content.startswith("$x"):
        keys = str(message.content).lower().split(" ")
        if str(message.content) == "$x r":
            await message.channel.send("https://xkcd.com/" + str(random.randint(1,len(comicdata)-1)))
            return
        if str(message.content) == "$x u":
            url = 'https://xkcd.com/archive/'

            # Connect to the URL
            response = requests.get(url)
            comicdata = []
            # Parse HTML and save to BeautifulSoup objectÂ¶

            tags =  response.text.split('(Hover mouse over title to view publication date)<br /><br />')[1]

            tags = tags.split('</div>')[0]
            tags = tags.split('<br/>')[:-1]


            for i in tags:
                comicname = re.search(">[\S\w\s]*<",i)[0][1:-1].lower()
                comicnum =  re.search("/\d*/", i )[0][1:-1].lower()
                comicdata.append([comicname,comicnum])
            comicdata.reverse()
            await message.channel.send("XKCD database Updated!s")
            await message.channel.send("https://xkcd.com/" + str(len(comicdata)+1))
            return
        if len(keys) ==1:
            await message.channel.send("https://xkcd.com/"+ comicdata[-1][1])
        else:
            print(keys)
            comics = collections.Counter()
            for i in comicdata:
                for j in keys:
                    if ( j ) in ( i[0] ):
                        comics[i[1]] +=1
            returned = comics.most_common()
            if len(returned) == 1:
                await message.channel.send("https://xkcd.com/" + returned[0][0])
            elif returned[0][1] > returned[1][1]:
                await message.channel.send("https://xkcd.com/" + returned[0][0])
            else:
                if len(returned) >3:
                    returned = returned[0:3]
                for i in returned:
                    print(i)
                    await message.channel.send("https://xkcd.com/"+ i[0])
        print(True)
    if message.content.startswith("$c4"):
        lowerline = ":black_circle:"*dp + ":white_circle:" + ":black_circle:" * (6-dp)
        await client.get_channel("int, game chat id").send("Welcome to Connect 4, " + message.mentions[0].mention + " and " + message.author.mention)
        p1 = message.mentions[0]
        p2 = message.author
        board = c4.C4()
        player = p1
        boardm = await client.get_channel("int, game chat id").send(str(board) + "\n" + lowerline)
        await boardm.add_reaction("⬅")
        await boardm.add_reaction("⬇")
        await boardm.add_reaction("➡")
        dp = 0
        turnm = await client.get_channel("int, game chat id").send(p1.mention + ", Its your turn!")

    if message.content.startswith('$hello'):
        await message.channel.send('Hello!')
    if message.content.startswith("$addbook"):
        pins = await client.get_channel("int,main chat id").pins()
        message = pins[0]
        await client.get_channel("int, save chat id").send("\"" + str(message.content) + "\" - " +
str(message.author.name))

    if message.content.startswith("$battleship"):
        await client.get_channel("int, game chat id").send("Welcome to sea battle, " +
message.mentions[0].mention + " and " + message.author.mention)

        p1 = message.mentions[0]
        p2 = message.author
        p1dm = p1.dm_channel
        if p1dm ==None:
            await p1.create_dm()
            p1dm = p1.dm_channel
        p2dm = p2.dm_channel
        if p2dm ==None:
            await p2.create_dm()
            p2dm = p2.dm_channel

        aboard = game.boarda.board


        bboard = game.boardb.board
        for i in aboard:
            for j in aboard:
                pass
        atemp = ""
        board1m = await p1dm.send(aboard)
        board2m = await p2dm.send(bboard)



          #                    :arrow_up: :arrow_down: :arrow_right:




@client.event
async def on_reaction_add(reaction, user):


    #add this!!
    global boardm, p1, p2, player, dp, board, turnm
    lowerline = ":black_circle:"*dp + ":white_circle:" + ":black_circle:" * (6-dp)
    #print(reaction.message, user)
    if user != client.user:
        #print(boardm)

        if reaction.emoji == "📖":
            pass
            # !! uncomment this later
            await reaction.message.channel.send("heading to the book")
            await client.get_channel("int, save chat id").send("\""+str(reaction.message.content)+"\" - " + str(reaction.message.author.name))
        elif reaction.message.id == boardm.id and user.id == player.id:
            await reaction.message.remove_reaction(reaction.emoji,user)
            if reaction.emoji == "⬅":
                dp -=1
                dp = dp%7
                print(dp)
                lowerline = ":black_circle:"*dp + ":white_circle:" + ":black_circle:" * (6-dp)
                await boardm.edit(content=(str(board) + "\n" + lowerline))

            elif reaction.emoji == "➡":
                dp +=1
                dp =  dp %7
                print(dp)
                lowerline = ":black_circle:"*dp + ":white_circle:" + ":black_circle:" * (6-dp)
                await boardm.edit(content=(str(board) + "\n" + lowerline))

            elif reaction.emoji == "⬇":
                if player == p1:
                    board.addp1(dp)
                    player = p2
                    await turnm.delete()
                    turnm = await client.get_channel("int, game chat id").send(p2.mention + ", Its your turn!")
                else:
                    board.addp2(dp)
                    player = p1
                    await turnm.delete()
                    turnm = await client.get_channel("int, game chat id").send(p1.mention + ", Its your turn!")
                await boardm.edit(content = (str(board) + "\n" + lowerline))
                print( board.checkall())
                if board.checkall() != None:
                    winner = board.checkall()
                    if winner == 1:
                        await client.get_channel("int, game chat id").send("Winner!!" + p1.mention)
                    else:
                        await client.get_channel("int, game chat id").send("Winner!!" + p2.mention)
                    boardm = None
            print("react")
        elif reaction.message == boardm:
            await reaction.message.remove_reaction(reaction.emoji,user)
        else:
            pass
            #await reaction.message.channel.send('{0} has reacted with {1.emoji}!'.format(user, reaction))
            #await reaction.message.remove_reaction(reaction.emoji,user)

@client.event
async def on_channel_pins_update(channel,message):
    await message.channel.send("heading to the book")
    await client.get_channel("int, save chat id").send("\"" + str(message.content) + "\" - " +
str(message.author.name))

client.run('INSERT CLIENT SECRET')
