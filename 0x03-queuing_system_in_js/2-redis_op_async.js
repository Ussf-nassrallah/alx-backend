/* Node Redis client and basic operations */

import redis from 'redis';

const client = redis.createClient();

const setNewSchool = (schoolName, value) => {
  // Set a key-value pair
  client.set(schoolName, value, redis.print);
};

const displaySchoolValue = (schoolName) => {
  // display the value of the key passed
  client.get(schoolName, (err, value) => {
    if (err) {
      console.log(err);
      return;
    };
    console.log(value);
  });
}

const main = async () => {
  await displaySchoolValue('Holberton');
  setNewSchool('HolbertonSanFrancisco', '100');
  await displaySchoolValue('HolbertonSanFrancisco');
};

client.on('connect', async () => {
  console.log('Redis client connected to the server');
  await main();
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});
