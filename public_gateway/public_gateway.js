const express = require('express');
const axios = require('axios');

const app = express();
const USER_SERVICE_URL = `http://user_service:${process.env.USER_SERVICE_PORT}`;
const AUTH_SERVICE_URL = `http://auth_service:${process.env.AUTH_SERVICE_PORT}`;

app.get('/user/:id', async (req, res) => {
  try {
    const userResponse = await axios.get(`${USER_SERVICE_URL}/user/${req.params.id}`);
    res.json(userResponse.data);
  } catch (error) {
    res.status(500).json({ error: 'Error fetching user data' });
  }
});

app.get('/auth/:id', async (req, res) => {
  try {
    const authResponse = await axios.get(`${AUTH_SERVICE_URL}/auth/${req.params.id}`);
    res.json(authResponse.data);
  } catch (error) {
    res.status(500).send('Error communicating with auth_service');
  }
});

app.listen(process.env.PUBLIC_GATEWAY_PORT, () => {
  console.log(`Public Gateway running on port ${process.env.PUBLIC_GATEWAY_PORT}`);
});
