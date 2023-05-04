const { REST, Routes } = require('discord.js');
const dotenv = require('dotenv');

dotenv.config();

const commands = [
  {
    name: 'ping',
    description: 'Pings the bot and shows the latency',
  },
  {
    name: 'random',
    description: 'Random number 1 to 50',
  },
  {
    name: 'help',
    description: 'Get help command',
  },
  {
    name: 'namebot',
    description: 'Name of bot',
  },
  {
    name: 'react',
    description: 'bot',
  },
];

const rest = new REST({ version: '10' }).setToken(process.env.TOKEN);

(async () => {
  try {
    console.log('Started refreshing application (/) commands.');

    await rest.put(Routes.applicationCommands(process.env.ClientID), { body: commands });

    console.log('Successfully reloaded application (/) commands.');
  } catch (error) {
    console.error(error);
  }
})();