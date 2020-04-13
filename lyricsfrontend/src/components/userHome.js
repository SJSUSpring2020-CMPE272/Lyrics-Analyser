import React, { Component } from 'react';
import { Input, Card, Button, Row, Col } from 'antd';
import axios from 'axios';
import valuesExport from '../config/config';
import { Redirect } from 'react-router';
import moment from 'moment';

const { TextArea } = Input;

class UserHome extends Component {

    constructor(){
        super();
        this.state={
            stringValue:'',
            lyricsSearched:[],
        }   

    }

    async componentDidMount(){
        await axios.get(valuesExport.url  + 'user/pastSearch/' + localStorage.getItem('user_id'))
    .then((response) => {
      if (response.status === 200) {
          console.log(JSON.stringify(response.data.searchValues))
        if(response.data.searchValues.length){
            this.setState({
                lyricsSearched:response.data.searchValues
            })
          }
      }
      else{
        
      }
    })
    .catch((e)=> {

    })
}
    getStringValue = (e) => {
        this.setState({
            stringValue:e.target.value
        })
    }

    submitClicked = () => {
        let values = {string:this.state.stringValue, user_id:localStorage.getItem('user_id'), date:moment().format('YYYY/MM/DD') };
        console.log(values)
        axios.post(valuesExport.url + 'user/searchString/', JSON.stringify(values), {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',

            }
        })
            .then(async res => {
                if (res.status >= 400) {
                    console.log(res)

                }
                else {
                  
                    await axios.get(valuesExport.url  + 'user/pastSearch/' + localStorage.getItem('user_id'))
                    .then((response) => {
                      if (response.status === 200) {
                          console.log(JSON.stringify(response.data.searchValues))
                        if(response.data.searchValues.length){
                            this.setState({
                                lyricsSearched:response.data.searchValues
                            })
                          }
                      }
                      else{
                        
                      }
                    })
                    .catch((e)=> {
                
                    })
                }
            })
            .catch(err => {
                console.log(err)
              
            })

    }



    render() {

        let name = 'Welcome '+localStorage.getItem('name')
        return (
            <div>
                <div>
                    <div style={{marginTop:'2%', marginLeft:'2%'}}>
                        <Row>
                            <Col span={11}>
                        <Card title={name} style={{ textAlign:'center'}}>
                            <Card.Grid style={{ width: '100%' }}>

                            <h3>Please enter lyrics string: </h3>
                            <TextArea rows={4} onChange={this.getStringValue} />
                            <Button type="primary" style={{marginTop:'2%'}} onClick={this.submitClicked}>Submit</Button>
                            </Card.Grid>
                        </Card>
                        </Col>
                    <Col span={1}></Col>
                        <Col span={12}>
                        <Card title='Your journey with us...'    hoverable
>
                           

                           
                            {console.log(this.state.lyricsSearched)}
                            {this.state.lyricsSearched.map((val, ind) =>{

                            return    <div key={ind}>
                                 <Card.Grid style={{ width: '100%' }} hoverable>
                                <Row>
                                    <Col span = {8}>
                               <h3>Lyrics searched: </h3>  
                                   </Col> 
                                   <Col span = {16}>
                                   <h3>{val.lyrics}</h3>
                                   </Col>
                               </Row>
                               <Row>
                               <Col span = {8}>

                               <h3>Date: </h3>   
                               </Col>
                               <Col span = {8}>
                               <h4>{moment(val.date).format('MMM')+' '+moment(val.date).format('DD')+', '
                               +moment(val.date).format('YYYY')}</h4> 
                               </Col>
                               </Row>
                               </Card.Grid>
                                </div>

                            })}
                        </Card>
                        </Col>

                        </Row>
                    </div>
                </div>

            </div>
        )
    }
}

export default UserHome;
