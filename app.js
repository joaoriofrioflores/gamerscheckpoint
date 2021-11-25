const path = require('path')
const express =require('express')
const logger = require('morgan')
const bodyParser = require('body-parser')

const app=express();
const { urlencoded } = require('express');
const indexRouters = require('./index')

app.set('port', 3000)
app.set('views', __dirname)
app.set('view engine', 'ejs')

app.use(logger('dev'))
app.use(bodyParser,urlencoded({extender:false}))

app.listen(app.get('port'), ()=>{
    console.log("SERVIDOR ACTIVADO Y EJECUTANDOSE")
})