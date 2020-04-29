import React, { Component } from 'react';
import { Input, Card, Button, Row, Col } from 'antd';
import axios from 'axios';
import valuesExport from '../config/config';
import { Redirect } from 'react-router';
import moment from 'moment';
import Table from './table.js';


const { TextArea } = Input;

class Journey extends Component {

    constructor() {
        super();
        this.state = {
            stringValue: '',
            lyricsSearched: [],
            tableData: [],
            normTableData: [],
            wordCloudArray: [],
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




    render() {

        let name = 'Welcome ' + localStorage.getItem('name')
        let title = "Your journey with us..."

        return (
            <div>
                <div>
                    <div style={{ marginTop: '2%', marginLeft: '2%' }}>
                        <Row>

                        </Row>

                        <Row>
                            <Col span={1}></Col>
                            <Col span={22}>
                                <Card title={<h3 style={{ color: '#822323e3', fontSize: 'cursive', fontFamily: 'unset', marginLeft: '35%' }}><strong>{title}</strong></h3>} hoverable >
                                    {this.state.lyricsSearched.map((val, ind) => {
                                        return <div key={ind}>
                                            <Card.Grid style={{ width: '100%' }} hoverable>
                                                <Row>
                                                    <Col span={8}>
                                                        <h3>Lyrics searched: </h3>
                                                    </Col>
                                                    <Col span={16}>
                                                        <h3 style={{fontFamily: 'unset', color:'#090956'}}><strong>{val.lyrics}</strong></h3>
                                                    </Col>
                                                </Row>
                                                <Row>
                                                    <Col span={8}>

                                                        <h3>Date: </h3>
                                                    </Col>
                                                    <Col span={8}>
                                                        <h4>{moment(val.date).format('MMM') + ' ' + moment(val.date).format('DD') + ', '
                                                            + moment(val.date).format('YYYY')}</h4>
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

export default Journey;
