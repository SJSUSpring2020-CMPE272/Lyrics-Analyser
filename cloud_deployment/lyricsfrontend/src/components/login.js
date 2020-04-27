import React, { Component } from 'react';
import { Form, Input, Button, Alert, Select } from 'antd';
import "antd/dist/antd.css";
import Headers from './header';
import Footer from './footer';
import axios from 'axios';
import valuesExport from '../config/config';
import { Redirect } from 'react-router';


const { Option } = Select;


class Login extends Component {
    constructor() {
        super();
        this.state = {

            redirectPage: '',
            showError: false,
        };
    }

    componentDidMount() {

    }

    handleSubmit = values => {
        console.log(values)

        axios.post(valuesExport.url + 'user/login/', JSON.stringify(values), {
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',

            }
        })
            .then(async res => {
                if (res.status >= 400) {
                    console.log(res)

                    this.setState({
                        showError: true,
                    })

                }
                else {

                   await  localStorage.setItem("user_id", res.data._id);
                    await localStorage.setItem("name", res.data.name);

this.setState({
    redirectPage: <Redirect to={{ pathname: '/user/home/' }} />
})

                }
            })
            .catch(err => {
                console.log(err)
                this.setState({
                    showError: true,
                })

            })
    }

    failedSubmit = (error) => {
        console.log(error)
    }

    render() {
        const frontFormLayout = {
            labelCol: {
                span: 8,
            },
            wrapperCol: {
                span: 8,
            },
        };
        const tailFormLayout = {
            wrapperCol: {
                offset: 8,
                span: 8,
            },
        };


        return (
            <div>
                {this.state.redirectPage}
                <div>
                    <Headers selectedKey={['3']} />
                </div>
                <div>

                    <Form
                        {...frontFormLayout}
                        name="basic"
                        initialValues={{
                            remember: true,
                        }}
                        onFinish={this.handleSubmit}
                        onFinishFailed={this.failedSubmit}
                        style={{ paddingTop: '2%' }}
                    >
                        <Form.Item
                            label="Email ID"
                            name="emailid"
                            rules={[
                                {
                                    required: true,
                                    message: 'Please input your emailID!',
                                },
                            ]}
                        >
                            <Input />
                        </Form.Item>

                        <Form.Item
                            label="Password"
                            name="password"
                            rules={[
                                {
                                    required: true,
                                    message: 'Please input your password!',
                                },
                            ]}
                        >
                            <Input.Password />
                        </Form.Item>

                        <Form.Item {...tailFormLayout}>
                            <Button type="primary" htmlType="submit">
                                Submit
        </Button>
                        </Form.Item>
                    </Form>
                </div>
                {this.state.showError && <div>
                    <Alert message="Invalid credentials" type="error" />

                </div>
                }
                <div>
                    <Footer />
                </div>

            </div>
        );
    }
}

export default Login;
