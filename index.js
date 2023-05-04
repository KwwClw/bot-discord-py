const { Client, Events, GatewayIntentBits, Message, Collection } = require('discord.js');
const client = new Client({ intents: [GatewayIntentBits.Guilds, GatewayIntentBits.GuildMessages, GatewayIntentBits.GuildMessageReactions] });
const dotenv = require('dotenv');
const { EmbedBuilder } = require('discord.js');


const helpEmbed = new EmbedBuilder()
  .setColor(0x91D8E4)
  .setTitle('Shenhe Bot help')
  .setURL('https://web-discord.kwwclw.repl.co/#')
  .setAuthor({ name: 'Shenhe', iconURL: 'https://www.linkpicture.com/q/579503ddd342c1a1891fac0b46434f77.jpg', url: 'https://discord.js.org' })
  .setDescription('All available bot commands')
  .setThumbnail('https://www.linkpicture.com/q/579503ddd342c1a1891fac0b46434f77.jpg')
  .addFields(
    { name: 'help', value: 'Get help command' },
    { name: 'namebot', value: 'Name of bot' },
    { name: 'random', value: 'Random number 1 to 50' },
    { name: 'Ping', value: 'Pings the bot and shows the latency' },
    // { name: '\u200B', value: '\u200B' },
    // { name: 'Inline field title', value: 'Some value here', inline: true },
    // { name: 'Inline field title', value: 'Some value here', inline: true },
  )
  .addFields({ name: 'Inline field title', value: 'Some value here', inline: true })
  .setImage('https://cdn.mos.cms.futurecdn.net/R5yrZcLCY8EmmWY5NwK2qP-970-80.jpg.webp')
  .setTimestamp()
  .setFooter({ text: 'Some footer text here', iconURL: 'https://www.linkpicture.com/q/579503ddd342c1a1891fac0b46434f77.jpg' });

// channel.send({ embeds: [exampleEmbed] });

dotenv.config();

client.on('ready', () => {
  console.log(`Logged in as ${client.user.tag}!`);
});

const menu = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "10", "11", "12", "13", "15", "16", "17", "18", "19", "20", "21", "22", "23", "24", "25", "26","27", "28", "29", "30", "31", "32", "33", "34", "35", "36", "37", "38", "39", "40", "41", "42", "43", "44", "45", "46", "47", "48", "49", "50"];

client.on('interactionCreate', async interaction => {
  if (!interaction.isChatInputCommand()) return;

  if (interaction.commandName === 'ping') {
    await interaction.reply(`Latency is ${Date.now() - interaction.createdTimestamp}ms. API Latency is ${Math.round(client.ws.ping)}ms`);
  }
  if (interaction.commandName === 'random') {
    await interaction.reply(menu[Math.floor(Math.random() * menu.length)]);
  }
  if (interaction.commandName === 'namebot') {
    await interaction.reply(`My name is ${client.user}`);
  }
  if (interaction.commandName === 'help') {
    await interaction.reply({ embeds: [helpEmbed] });
  }
  if (interaction.commandName === 'react') {
    const message = await interaction.reply({ content: 'You can react with Unicode emojis!', fetchReply: true });
    message.react('😐');
  }
});

client.login(process.env.TOKEN);