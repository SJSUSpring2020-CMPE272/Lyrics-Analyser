import React, { Component } from 'react';
import { Input, Card, Button, Row, Col } from 'antd';
import axios from 'axios';
import valuesExport from '../config/config';
import { Redirect } from 'react-router';
import moment from 'moment';
import Table from './table.js';
import { trackPromise } from 'react-promise-tracker';
import WordCloud from "react-d3-cloud";
import { XYPlot, XAxis, YAxis, HorizontalGridLines, MarkSeries, VerticalBarSeries } from 'react-vis';

const { TextArea } = Input;
const fontSizeMapper = word => Math.log2(word.value) * 5;

class UserHome extends Component {

    constructor() {
        super();
        this.state = {
            stringValue: '',
            lyricsSearched: [],
            tableData: [],
            normTableData: [],
            wordCloudArray: [],
            barGraphArray: [],
        }
    }

    async componentDidMount() {
        await axios.get(valuesExport.url + 'user/pastSearch/' + localStorage.getItem('user_id'))
            .then((response) => {
                if (response.status === 200) {
                    if (response.data.searchValues.length) {
                        this.setState({
                            lyricsSearched: response.data.searchValues
                        })
                    }
                }
                else {

                }
            })
            .catch((e) => {

            })
    }
    getStringValue = (e) => {
        this.setState({
            stringValue: e.target.value
        })
    }

    submitClicked = () => {
        this.state.tableData = []
        this.state.normTableData = []
        this.state.wordCloudArray = []
        let values = { string: this.state.stringValue, user_id: localStorage.getItem('user_id'), date: moment().format('YYYY/MM/DD') };
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

                    /*
                    {x: 'Length', y: 142},
            {x: 'Most', y: 15},
            {x: 'Average', y: 9},
            {x: 'Unique', y: 68},
            {x: 'WeightLength', y: 43},
            {x: 'WeightUnique', y: 68}  
            */

                    // populate the bar graph data
                    /*
                    "User Graph Features":
            Length: 137
            Most: 19
            Average: 12.6
            Unique: 59
            WeightLength: 15.9
            WeightUnique: 25.23
                    */
                    var userGraphFeatures = res.data["User Graph Features"]
                    this.state.barGraphArray.push({ x: 'Length', y: userGraphFeatures["Length"] })
                    this.state.barGraphArray.push({ x: 'Most', y: userGraphFeatures["Most"] })
                    this.state.barGraphArray.push({ x: 'Average', y: userGraphFeatures["Average"] })
                    this.state.barGraphArray.push({ x: 'Unique', y: userGraphFeatures["Unique"] })
                    this.state.barGraphArray.push({ x: 'WeightLength', y: userGraphFeatures["WeightLength"] })
                    this.state.barGraphArray.push({ x: 'WeightUnique', y: userGraphFeatures["WeightUnique"] })

                    console.log(this.state.barGraphArray)
                    console.log(JSON.stringify(this.state.barGraphArray))
                    var popular = "Not Popular";
                    var value = res.data['Absolute RFC CLASSIFICATION']
                    value = value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"
                    this.state.tableData.push({ 'Algorithm': "Absolute RFC CLASSIFICATION", 'Value': res.data['Absolute RFC CLASSIFICATION'], 'Popular/Not Popular': popular, 'Accuracy': res.data['Absolute RF Accuracy'] });

                    popular = "Not Popular";
                    value = res.data['Absolute RFR REGRESSION']
                    value = value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"

                    this.state.tableData.push({ 'Algorithm': "Absolute RFR REGRESSION", 'Value': res.data['Absolute RFR REGRESSION'], 'Popular/Not Popular': popular, 'Accuracy': res.data['Absolute RF Accuracy'] });

                    popular = "Not Popular";
                    value = res.data['Absolute KNN CLASSIFICATION']
                    value = value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"

                    this.state.tableData.push({ 'Algorithm': "Absolute KNN CLASSIFICATION", 'Value': res.data['Absolute KNN CLASSIFICATION'], 'Popular/Not Popular': popular, 'Accuracy': res.data['KNN Accuracy'] });

                    popular = "Not Popular";
                    value = res.data['Absolute LRC']
                    value = value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"
                    this.state.tableData.push({ 'Algorithm': "Absolute LRC", 'Value': res.data['Absolute LRC'], 'Popular/Not Popular': popular, 'Accuracy': res.data['LRC Accuracy'] });

                    popular = "Not Popular";
                    value = res.data['Normalized RFC CLASSIFICATION']
                    //  value=value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"
                    this.state.normTableData.push({ 'Algorithm': "Normalized RFC CLASSIFICATION", 'Value': res.data['Normalized RFC CLASSIFICATION'], 'Popular/Not Popular': popular, 'Accuracy': res.data['Normalized RF Accuracy'] });

                    popular = "Not Popular";
                    value = res.data['Normalized RFR REGRESSION']
                    value = value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"

                    this.state.normTableData.push({ 'Algorithm': "Normalized RFR REGRESSION", 'Value': res.data['Normalized RFR REGRESSION'], 'Popular/Not Popular': popular, 'Accuracy': res.data['Normalized RF Accuracy'] });

                    popular = "Not Popular";
                    value = res.data['Normalized KNN CLASSIFICATION']
                    value = value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"

                    this.state.normTableData.push({ 'Algorithm': "Normalized KNN CLASSIFICATION", 'Value': res.data['Normalized KNN CLASSIFICATION'], 'Popular/Not Popular': popular, 'Accuracy': res.data['KNN Accuracy'] });

                    popular = "Not Popular";
                    value = res.data['Normalized LRC']
                    value = value.replace(/[\[\]]/g, "");
                    if (parseFloat(value) >= .5)
                        popular = "Popular"
                    this.state.normTableData.push({ 'Algorithm': "Normalized LRC", 'Value': res.data['Normalized LRC'], 'Popular/Not Popular': popular, 'Accuracy': res.data['LRC Accuracy'] });


                    //get the wordcloud data
                    var array = res.data["User Wordcloud"]
                    array.forEach(item => this.state.wordCloudArray.push({ text: item['text'], value: 100 }))
                    this.setState({
                        tableData: this.state.tableData,
                        normTableData: this.state.normTableData,
                        wordCloudArray: this.state.wordCloudArray,
                        barGraphArray: this.state.barGraphArray
                    })

                    // await axios.get(valuesExport.url + 'user/pastSearch/' + localStorage.getItem('user_id'))
                    //     .then((response) => {
                    //         if (response.status === 200) {
                    //             if (response.data.searchValues.length) {
                    //                 this.setState({
                    //                     lyricsSearched: response.data.searchValues
                    //                 })
                    //             }
                    //         }
                    //         else {

                    //         }
                    //     })
                    //     .catch((e) => {

                    //     })
                }
            })
            .catch(err => {
                console.log(err)

            }));

    }



    render() {

        let name = 'Welcome ' + localStorage.getItem('name')
        let myComponent;
        if (this.state.tableData.length > 0) {
            myComponent = <Table data={this.state.tableData} />
        } else {
            myComponent = null
        }

        let normComponent;
        if (this.state.normTableData.length > 0) {
            normComponent = <Table data={this.state.normTableData} />
        } else {
            normComponent = null
        }

        let wordCloudComponent;
        if (this.state.wordCloudArray.length > 0) {
            wordCloudComponent = <WordCloud data={this.state.wordCloudArray} fontSizeMapper={fontSizeMapper} width="500" height="500" />
        } else {
            wordCloudComponent = null
        }
        let barGraphComponent;
        if (this.state.barGraphArray.length > 0) {
            barGraphComponent = <React.Fragment>
                <XYPlot xType="ordinal"
                    width={500}
                    height={250}>
                    <XAxis>Features in Dataset</XAxis>
                    <YAxis>Average</YAxis>
                    <VerticalBarSeries
                        className="bar-series-example"
                        data={this.state.barGraphArray} />
                </XYPlot>
            </React.Fragment>
        } else {
            barGraphComponent = null
        }
        return (
            <div>
                <div>
                    <div style={{ marginTop: '2%', marginLeft: '2%' }}>
                   

                        <Row>
                            <Col span={11}>
                                <Card title={name} style={{ textAlign: 'center', fontSize: '32px' }}>
                                    <Card.Grid style={{ width: '100%' }}>
                                        <h3 style={{ font: 'italic bold 20px/30px Georgia, serif' }}>Please enter lyrics string: </h3>
                                        <TextArea rows={4} onChange={this.getStringValue} />
                                        <Button type="primary" style={{ marginTop: '2%' }} onClick={this.submitClicked}>Submit</Button>
                                    </Card.Grid>
                                </Card>
                            </Col>
                            <Col span={11}>{barGraphComponent}</Col>


                        </Row>
                        <Row>
                            <Col span={22}>
                               { wordCloudComponent && <Card style={{ textAlign: 'center' }}>
                                    <Card.Grid style={{ width: '100%' }}>
                                        {wordCloudComponent}
                                    </Card.Grid>
                                </Card>
    }
                            </Col>


                        </Row>
                        <Row>

                            <Col span={11}>
                               {myComponent && <Card style={{ textAlign: 'center' }}>
                                    <Card.Grid style={{ width: '100%' }}>
                                        {myComponent}
                                    </Card.Grid>
                                </Card>
    }

                            </Col>

                            <Col span={11}>
                              {normComponent &&  <Card style={{ textAlign: 'center' }}>
                                    <Card.Grid style={{ width: '100%' }}>
                                        {normComponent}
                                    </Card.Grid>
                                </Card>
    }
                            </Col>
                        </Row>

                    </div>

                </div>


            </div>
        )
    }
}

export default UserHome;
