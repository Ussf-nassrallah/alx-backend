#!/usr/bin/yarn dev
import express from 'express';
import { promisify } from 'util';
import { createClient } from 'redis';

const productsList = [
  {
    id: 1,
    name: 'Suitcase 250',
    price: 50,
    initialQuantity: 4
  },
  {
    id: 2,
    name: 'Suitcase 450',
    price: 100,
    initialQuantity: 10
  },
  {
    id: 3,
    name: 'Suitcase 650',
    price: 350,
    initialQuantity: 2
  },
  {
    id: 4,
    name: 'Suitcase 1050',
    price: 550,
    initialQuantity: 5
  },
];

const getProductById = (productId) => {
  const product = productsList.find(item => item.id === productId);

  if (product) {
    return { ...product };
  }
};

const app = express();
const redisClient = createClient();
const PORT = 1245;

const reserveStockById = async (productId, stock) => {
  return promisify(redisClient.SET).bind(redisClient)(`product.${productId}`, stock);
};

const getCurrentReservedStockById = async (productId) => {
  return promisify(redisClient.GET).bind(redisClient)(`product.${productId}`);
};

app.get('/list_products', (_, res) => {
  res.json(productsList);
});

app.get('/list_products/:productId(\\d+)', (req, res) => {
  const productId = Number.parseInt(req.params.productId);
  const product = getProductById(productId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  getCurrentReservedStockById(productId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
      product.currentQuantity = product.initialQuantity - reservedStock;
      res.json(product);
    });
});

app.get('/reserve_product/:productId', (req, res) => {
  const productId = Number.parseInt(req.params.productId);
  const product = getProductById(productId);

  if (!product) {
    res.json({ status: 'Product not found' });
    return;
  }

  getCurrentReservedStockById(productId)
    .then((result) => Number.parseInt(result || 0))
    .then((reservedStock) => {
      if (reservedStock >= product.initialQuantity) {
        res.json({ status: 'Not enough stock available', productId });
        return;
      }

      reserveStockById(productId, reservedStock + 1)
        .then(() => {
          res.json({ status: 'Reservation confirmed', productId });
        });
    });
});

const resetProductsStock = () => {
  return Promise.all(
    productsList.map(
      item => promisify(redisClient.SET).bind(redisClient)(`product.${item.id}`, 0),
    )
  );
};

app.listen(PORT, () => {
  resetProductsStock()
    .then(() => {
      console.log(`API available on localhost port ${PORT}`);
    });
});

export default app;
