import React, { Component } from 'react';
import Footer from './footer';
import Headers from './header';
import { Layout, Row, Col, Carousel, Card } from 'antd';
import "antd/dist/antd.css";

//import './../index.css'

const { Content } = Layout;


class WelcomePage extends Component {
    constructor() {
        super();
        this.state = {
            redirect: ''
        };
    }

    componentDidMount() {
        localStorage.clear();
    }


    render() {

        return (
            <div>
                <div>
                
                    <Row >
                        <Layout className="layout">
                            <Headers selectedKey={['1']} />
                            <Content style={{ background: 'yellow' }}>
                                <div style={{ backgroundColor: 'yellow' }}>
                                    <br></br>

                                    <Row>
                                        <Col span={6}>

                                            <img src={require('../images/sixth.png')} style={{ maxWidth: '100%', minHeight: '100%', maxHeight: '20%' }} />
                                        </Col>
                                       
                                        <Col span={6}>
                                            <img src={require('../images/fourth.jpeg')} style={{ maxWidth: '100%', minHeight: '100%', maxHeight: '20%' }} />
                                        </Col>
                                       
                                        
                                        <Col span={6}>
                                            <img src={require('../images/fifth.png')} style={{ maxWidth: '100%', minHeight: '100%', maxHeight: '20%' }} />
                                        </Col>
                                                                               <Col span={6}>
                                            <img src={require('../images/third.jpeg')} style={{ maxWidth: '100%', minHeight: '100%', maxHeight: '20%' }} />
                                        </Col>
                                        
                                        {/* <Col span={2}></Col>
                                        <Col span={6}>
                                            <h1>Welcome to our Page!!</h1>

                                        </Col> */}
                                    </Row>
                                    <Row>

                                    </Row>
                                </div>

                            </Content>
                            <Footer />
                        </Layout>

                    </Row>
                </div>
           
            </div>
        );
    }
}

export default WelcomePage;
