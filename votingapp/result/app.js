const express = require('express');
const { Client } = require('pg');

const app = express();

const client = new Client({
    host: 'db-service',
    user: 'postgres',
    password: 'postgres',
    database: 'votes'
});

client.connect();

app.get('/', async(req,res)=>{

    const result = await client.query(
        'select * from votes'
    ).catch(()=>({rows:[]}));

    res.send(result.rows);
});

app.listen(80);