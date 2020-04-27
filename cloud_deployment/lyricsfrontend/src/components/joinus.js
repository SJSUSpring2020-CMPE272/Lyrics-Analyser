
import React from 'react';
import "antd/dist/antd.css";
import moment from 'moment';
import Headers from './header';
import Footer from './footer';
import Swal from 'sweetalert2';
import valuesExport from '../config/config';
import axios from 'axios';
import { Redirect } from 'react-router';


import {
    Form,
    Input,
    Select,
    Button,
} from 'antd';


const { Option } = Select;

class RegistrationForm extends React.Component {
    formRef = React.createRef();

    constructor() {
        super();
        this.state = {
            stateValue: '',
            showSubmit: false,
          
            redirectPage:'',
        }
    }

    componentDidMount(){
       
    }

    onStateChange = (value) => {
        this.setState({
            stateValue: value
        })

    }

    onFinish = values => {
        Swal.fire('Welcome','', 'success')
       
        var insertUser={
            name:values.username,
            emailid:values.email,
            password:values.password,
            date:moment().format('YYYY/MM/DD'),
        }
        axios.post(valuesExport.url + 'user/add/', JSON.stringify(insertUser), {
            headers: {
              'Accept': 'application/json',
              'Content-Type': 'application/json',
  
            }
          })
          .then(res => {
            if (res.status >= 400) {
            }
            else {
         
                this.setState({
                    redirectPage: <Redirect to={{ pathname: '/signin/' }} />
                    })
            }
          })
          .catch(err => {
           console.log(err)
          })
       

    };

    checkName = (rule, value) => {
        this.setState({
            name: value
        })
        return Promise.resolve()
    }

    checkValidity = (rule, value) => {
        let month = moment(value).format('MM');
        let year = moment(value).format('YY')
        let valueO = month + year
        this.setState({
            expiry: valueO
        })
        return Promise.resolve()

    }


    disabledDate = (current) => {
        return current && current.valueOf() < Date.now();

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
                    <Headers selectedKey={['2']} />
                </div>
                <div>
                <Form
                        {...frontFormLayout}
                        name="basic"
                        initialValues={{
                            remember: true,
                        }}
                        onFinish={this.onFinish}
                        style={{ paddingTop: '2%' }}
                    >
                         <Form.Item
                            name="username"
                            label="Username"
                            rules={[
                                {

                                },
                                {
                                    required: true,
                                    message: 'Please input your name!',
                                },
                            ]}
                        >
                            <Input />
                        </Form.Item>
                        <Form.Item
                            name="email"
                            label="E-mail"
                            rules={[
                                {
                                    type: 'email',
                                    message: 'The input is not valid E-mail!',
                                },
                                {
                                    required: true,
                                    message: 'Please input your E-mail!',
                                },
                            ]}
                        >
                            <Input />
                        </Form.Item>

                        <Form.Item
                            name="password"
                            label="Password"
                            rules={[
                                {
                                    required: true,
                                    message: 'Please input your password!',
                                },
                            ]}
                            hasFeedback
                        >
                            <Input.Password />
                        </Form.Item>

                        <Form.Item
                            name="confirm"
                            label="Confirm Password"
                            dependencies={['password']}
                            hasFeedback
                            rules={[
                                {
                                    required: true,
                                    message: 'Please confirm your password!',
                                },
                                ({ getFieldValue }) => ({
                                    validator(rule, value) {
                                        if (!value || getFieldValue('password') === value) {
                                            return Promise.resolve();
                                        }

                                        return Promise.reject('The two passwords that you entered do not match!');
                                    },
                                }),
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
                <div>
                    <Footer/>
                </div>


            </div>
        );
    }
};

export default RegistrationForm;