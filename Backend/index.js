var express = require('express');
var app = express();
var bodyParser = require('body-parser');
var cors = require('cors');
const user = require("./models/userModal");
var bcrypt = require('bcrypt');

app.set('view engine', 'ejs');


const config = require('./config/config.json');

const port = process.env.port || config.port;


app.use(express.json({ extended: false }));

//use cors to allow cross origin resource sharing
app.use(cors({ origin: config.frontendURL, credentials: true }));


app.use(bodyParser.json());

//Allow Access Control
app.use(function (req, res, next) {
    res.setHeader('Access-Control-Allow-Origin', config.frontendURL);
    res.setHeader('Access-Control-Allow-Credentials', 'true');
    res.setHeader('Access-Control-Allow-Methods', 'GET,HEAD,OPTIONS,POST,PUT,DELETE');
    res.setHeader('Access-Control-Allow-Headers', 'Access-Control-Allow-Headers, Origin,Accept, X-Requested-With, Content-Type, Access-Control-Request-Method, Access-Control-Request-Headers');
    res.setHeader('Cache-Control', 'no-cache');
    next();
});

const mongoose = require('mongoose');

console.log(config.mongoConn)
let options = {
    useNewUrlParser: true,
    useUnifiedTopology: true,
    poolSize: 200,
    bufferMaxEntries: 0,
    useCreateIndex: true

};

mongoose.connect(config.mongoConn, options, (err, res) => {
    if (err) {
        console.log(err);
        console.log(`MongoDB Connection Failed`);
    } else {
        console.log(`MongoDB Connected`);
    }
});




app.get('/', (req, res) => res.send('YO! RUNNING!'))


app.post('/user/add/', function (req, res) {
    console.log(req.body)
    user.findOne({ emailid: req.body.emailid }, async (error, emailid) => {
        console.log("finding emailid")

        if (error) {
            console.log(error)
            res.status(400).send('error');

        }
        if (emailid) {
            console.log("email id is not unique")
            res.status(400).send('error');


        }
        else {
            const salt = await bcrypt.genSalt(10);

            const encryptpassword = await bcrypt.hash(req.body.password, salt);

            var newUser = new user({
                name: req.body.name,
                emailid: req.body.emailid,
                password: encryptpassword,
                date: req.body.date
            });
            console.log(newUser)
            user.create(newUser, (error, data) => {
                if (error) {
                    res.status(400).send('error');

                }
                else {
                    res.setHeader('Content-Type', 'application/json');

                    res.status(200).send(data);

                }
            })


        }
    })
})

app.post('/user/login/', function (req, res) {
    console.log(req.body);
    user.findOne({ emailid: req.body.emailid },
        async (err, result) => {
            if (err) {
                res.status(400).send('error');

            }
            if (!result) {
                res.status(400).send('error');

            }
            console.log(result)
            const isMatch = await bcrypt.compare(req.body.password, result.password);
            console.log(isMatch)
            if (!isMatch) {
                res.status(400).send('error');

            }
            console.log("Values" + result)
            res.setHeader('Content-Type', 'application/json');

            res.status(200).send(result);

        }
    );
});

callPython = async (values) => {
    return new Promise(async function(resolve, reject){
        var spawn = require("child_process").spawn; 

        var dataToSend;
        // spawn new child process to call the python script
        const python = spawn('python', ['../NLP_ML/Python_File.py',
        values.string]);
        // collect data from script
        python.stdout.on('data', async function (data) {
         dataToSend = data.toString();
        });
        python.on('close', async (code) => {
        console.log(`child process close all stdio with code ${code}`);
        console.log(dataToSend)    
        resolve( dataToSend);
    })
    

    });

}

insertInDB = (values) => {
    return new Promise(async function(resolve, reject){

    user.findById(values.user_id,
        async (err, data) => {
            if (err) {
                reject('error')
            }
            if (!data) {
                reject('error')
            }

            data.updateOne({
                $push: {
                    'searchValues': {
                        lyrics: values.string,
                        date: values.dat,

                    }

                }

            }, function (err, result) {
                if (err) {

                    reject('error')
                }
                else {
                    resolve( result);



                }
            });

        }
    );
    });
}

app.post('/user/searchString/', async function (req, res) {
    console.log(req.body);


    let promise1 = callPython(req.body);
    let promise2 = insertInDB(req.body);

    Promise.all([promise1, promise2]).then((result)=>{
        res.status(200).send(result[0]);
    })
    .catch((e)=>{
        res.status(400).send('error');
    })
    
    
});


app.get('/user/pastSearch/:userid', function (req, res) {

    user.findById(req.params.userid, 'searchValues',
        async (err, data) => {
            if (err) {
                res.status(400).send('error');

            }
            else{
            console.log(JSON.stringify(data))
            res.setHeader('Content-Type', 'application/json');
            res.status(200).send(data);
            }
        }
    );
});


app.listen(port, () => console.log("Server Listening on port " + port))
