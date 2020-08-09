const Discord = require('discord.js');
const client = new Discord.Client();
const token = require('./token');
const gameTypes = {
    connect4:'connect4',
    any:"any"
}
gamesArr = [];
console.log(gamesArr);

console.log(token.token);
client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});


function getGame(uarr, findGameType=gameTypes.any){
    return gamesArr.find( game=> (game.gameType == findGameType || findGameType == gameTypes.any) && game.users.every(gameUsers=> uarr.some( uid=> uid==gameUsers.id)));
}

class game{
    constructor(users, gtype){
        this.users=users;
        this.gameType = gtype;
        this.id="";
    }
    setMessageId(id){
        this.id=id
    }
}

class connect4 extends game{
    constructor(users,gtype){
        super(users,gtype);
        this.board = []
        for(let i=0; i<6; i++){
            this.board.push(Array.apply(null, Array(5)).map(function () {}))
        }
        
    }
}

client.on('message', msg => {
  if (msg.content === 'ping') {
    msg.reply('pong');
  }

  console.log(msg.content)
  if (msg.content.startsWith("$c4") && msg.mentions.users.size==1){
      console.log("im doing something!");
      let user1= msg.author;
      let user2 = msg.mentions.users.values().next().value;
      let usersArr = [user1, user2];

      possiblegame = getGame(usersArr, gameTypes.connect4);
      console.log(possiblegame);
      if (typeof(possiblegame) == 'undefined'){
        possiblegame = gamesArr.push(new connect4([user1, user2], gameTypes.connect4));

        msg.reply("no game yet. ill make one for you")
        msg.channel.send("<@!"+user1+"> heres ur game with <@!"+ user2 + ">")

      }
      else{
          msg.reply("you already have a game. at some point theres gonna be a link to that");
      }
      
      
      console.log("found something")
  }
});

client.on('messageReactionAdd', async (reaction, user) => {
	// When we receive a reaction we check if the reaction is partial or not
	if (reaction.partial) {
		// If the message this reaction belongs to was removed the fetching might result in an API error, which we need to handle
		try {
			await reaction.fetch();
		} catch (error) {
			console.log('Something went wrong when fetching the message: ', error);
			// Return as `reaction.message.author` may be undefined/null
			return;
		}
	}
	// Now the message has been cached and is fully available
	console.log(`${reaction.message.author}'s message "${reaction.message.content}" gained a reaction!`);
	// The reaction is now also fully available and the properties will be reflected accurately:
    console.log(`${reaction.count} user(s) have given the same reaction to this message!`);
    console.log(`${reaction.emoji.name} was the emoji id  and the emoji was a thumbs up ? ${reaction.emoji.name == "👍"}`)
});

client.login(token.token);
