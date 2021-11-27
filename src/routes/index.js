const {render} = require('ejs');
const fs = require('fs')
const express = require('express')
const router = express.Router()

router.get('/', (req, res) =>{
    res.render('index')
})

//post para traer de carrito de compras que se conecte a la colleción



module.exports = router;