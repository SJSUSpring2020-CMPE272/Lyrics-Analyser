const mongoose = require('mongoose');
const Schema = mongoose.Schema;

var userSchema = new Schema({
    id:mongoose.Types.ObjectId,
    name: {type: String, required: true},
    emailid: {type: String, required: true, unique:true},
    password: {type: String, required: true},

    searchValues:[{
        searchid:mongoose.Types.ObjectId,
        lyrics:{type:String},
        date:Date,
      
    }],
   
},
{
    versionKey: false
});

module.exports = mongoose.model('user', userSchema);
