/* Node Redis client and basic operations */

import redis from 'redis';

const client = redis.createClient();

client.on('connect', () => {
  console.log('Redis client connected to the server');
});

client.on('error', (err) => {
  console.log(`Redis client not connected to the server: ${err}`);
});

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

displaySchoolValue('Holberton');
setNewSchool('HolbertonSanFrancisco', '100');
displaySchoolValue('HolbertonSanFrancisco');
