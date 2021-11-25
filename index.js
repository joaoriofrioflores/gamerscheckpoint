const express =require('express');
const router = express.Router();
const client = require('./db');

router.get('/', (req, res)=> {
    res.render('main')
})

module.exports = router;