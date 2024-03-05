// Node Redis client and advanced operations

import redis from 'redis';

const client = redis.createClient();

const hashSet = (hash, obj) => {
  for (const key in obj) {
    client.HSET(hash, key, obj[key], redis.print);
  };
};

client.on('connect', () => {
  console.log('Redis client connected to the server');

  const myObj = {
    'Portland': 50,
    'Seattle': 80,
    'New York': 20,
    'Bogota': 20,
    'Cali': 40,
    'Paris': 2
  };

  hashSet('HolbertonSchools', myObj);
  client.HGETALL('HolbertonSchools', (err, reply) => console.log(reply));
});

client.on('error', (error) => {
  console.log(`Redis client not connected to the server: ${error}`);
})
