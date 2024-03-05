const express = require("express");
const redis = require("redis");
import { promisify } from "util";

const app = express();
const client = redis.createClient();

app.use(express.json());

const listProducts = [
  {
    itemId: 1,
    itemName: "Suitcase 250",
    price: 50,
    initialAvailableQuantity: 4,
  },
  {
    itemId: 2,
    itemName: "Suitcase 450",
    price: 100,
    initialAvailableQuantity: 10,
  },
  {
    itemId: 3,
    itemName: "Suitcase 650",
    price: 350,
    initialAvailableQuantity: 2,
  },
  {
    itemId: 4,
    itemName: "Suitcase 1050",
    price: 550,
    initialAvailableQuantity: 5,
  },
];

function getItemById(id) {
  for (let item of listProducts) {
    if (item["itemId"] === id) return item;
  }
}

function reserveStockById(id, stock) {
  client.set(id, stock);
}

const get = promisify(client.get).bind(client);

async function getCurrentReservedStockById(id) {
  return await get(id);
}

app.get("/list_products", (req, res) => {
  res.json(listProducts);
});

app.get("/list_products/:itemId", (req, res) => {
  let itm = getItemById(Number(req.params.itemId));
  if (!itm) res.json({ status: "Product not found" });
  const currentQuantity = getCurrentReservedStockById(req.params.itemId);
  if (!currentQuantity) itm["currentQuantity"] = currentQuantity;
  else itm["currentQuantity"] = itm["initialAvailableQuantity"];
  res.json(itm);
});

app.get("/list_products/:itemId", (req, res) => {
  let itm = getItemById(Number(req.params.itemId));
  if (!itm) res.json({ status: "Product not found" });
  if (itm["initialAvailableQuantity"] <= 1)
    res.json({ status: "Not enough stock available", itemId: itm["itemId"] });
  reserveStockById(itm["itemId"], 1);
  res.json({ status: "Reservation confirmed", itemId: itm["itemId"] })
});

app.listen("1245");
