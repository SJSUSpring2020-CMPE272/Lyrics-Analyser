import React, { Component } from 'react';
import { Input, Card, Button, Row, Col } from 'antd';
import axios from 'axios';
import valuesExport from '../config/config';
import { Redirect } from 'react-router';
import moment from 'moment';
import Table from './table.js';
import { trackPromise } from 'react-promise-tracker';
import WordCloud from "react-d3-cloud";


const { TextArea } = Input;
const fontSizeMapper = word => Math.log2(word.value) * 5;

class UserHome extends Component {

    constructor(){
        super();
        this.state={
            stringValue:'',
            lyricsSearched:[],
			tableData:[],
			wordCloudArray: [],
        }
    }

    async componentDidMount(){
        await axios.get(valuesExport.url  + 'user/pastSearch/' + localStorage.getItem('user_id'))
    .then((response) => {
      if (response.status === 200) {
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
		this.state.tableData=[]
        let values = {string:this.state.stringValue, user_id:localStorage.getItem('user_id'), date:moment().format('YYYY/MM/DD') };
        console.log(values)
        	trackPromise(axios.post(valuesExport.url + 'user/searchString/', JSON.stringify(values), {
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
					console.log(JSON.stringify(res))
					var popular="Not Popular";
					var value=res.data['Absolute RFC CLASSIFICATION']
					value=value.replace(/[\[\]]/g, "");
					if(parseFloat(value) >= .5)
						popular="Popular"
					this.state.tableData.push({'Algorithm': "Absolute RFC CLASSIFICATION", 'Value': res.data['Absolute RFC CLASSIFICATION'], 'Popular/Not Popular': popular,'Accuracy': res.data['Absolute RF Accuracy'] });

					 popular="Not Popular";
					value=res.data['Absolute RFR REGRESSION']
					value=value.replace(/[\[\]]/g, "");
					if(parseFloat(value) >= .5)
						popular="Popular"

					this.state.tableData.push({'Algorithm': "Absolute RFR REGRESSION", 'Value': res.data['Absolute RFR REGRESSION'], 'Popular/Not Popular': popular,'Accuracy': res.data['Absolute RF Accuracy'] });

				 	popular="Not Popular";
					value=res.data['Absolute KNN CLASSIFICATION']
					value=value.replace(/[\[\]]/g, "");
					if(parseFloat(value) >= .5)
						popular="Popular"

					this.state.tableData.push({'Algorithm': "Absolute KNN CLASSIFICATION", 'Value': res.data['Absolute KNN CLASSIFICATION'], 'Popular/Not Popular': popular,'Accuracy': res.data['KNN Accuracy'] });

				 	popular="Not Popular";
					value=res.data['Absolute LRC']
					value=value.replace(/[\[\]]/g, "");
					if(parseFloat(value) >= .5)
						popular="Popular"
					this.state.tableData.push({'Algorithm': "Absolute LRC", 'Value': res.data['Absolute LRC'], 'Popular/Not Popular': popular,'Accuracy': res.data['LRC Accuracy'] });
					
					
					//get the wordcloud data
					var array=res.data["User Wordcloud"]
					array.forEach(item => this.state.wordCloudArray.push({text: item['text'], value: 100}))
                    this.setState({
						tableData:this.state.tableData,
						wordCloudArray: this.state.wordCloudArray
                    })
				
                    await axios.get(valuesExport.url  + 'user/pastSearch/' + localStorage.getItem('user_id'))
                    .then((response) => {
                      if (response.status === 200) {
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

            }));

    }



    render() {

        let name = 'Welcome '+localStorage.getItem('name')
		let myComponent;
		    if(this.state.tableData.length>0) {
		        myComponent = <Table data={this.state.tableData}/>
		    } else {
		        myComponent = null
		    }
			
		let wordCloudComponent;
			    if(this.state.wordCloudArray.length>0) {
			        wordCloudComponent = <WordCloud data= {this.state.wordCloudArray} fontSizeMapper={fontSizeMapper} width="500" height="500"/>
			    } else {
			        wordCloudComponent = null
			    }
        return (
            <div>
                <div>
                    <div style={{marginTop:'2%', marginLeft:'2%'}}>
                        <Row>
                            <Col span={11}>
                        <Card title={name} style={{ textAlign:'center', fontSize: '32px'}}>
                            <Card.Grid style={{ width: '100%' }}>
                            <h3 style={{font: 'italic bold 20px/30px Georgia, serif'}}>Please enter lyrics string: </h3>
                            <TextArea rows={4} onChange={this.getStringValue} />
                            <Button type="primary" style={{marginTop:'2%'}} onClick={this.submitClicked}>Submit</Button>
                            </Card.Grid>
                        </Card>
                        </Col>



            <Col span={11}>
        	<Card style={{ textAlign:'center'}}>
            <Card.Grid style={{ width: '100%' }}>
			{myComponent}
            </Card.Grid>
        </Card>
        </Col>


            </Row>
			<Row>
			{wordCloudComponent}

           	</Row>
						<Row>
    <Col span={1}></Col>
        <Col span={22}>
        <Card title='Your journey with us...'    hoverable>
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
