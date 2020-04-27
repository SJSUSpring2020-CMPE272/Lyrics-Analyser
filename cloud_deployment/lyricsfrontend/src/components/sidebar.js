import React from 'react';
import "antd/dist/antd.css";
import UserHeader from './userHeader'
import { Layout, Menu } from 'antd';
import {
  DesktopOutlined,
 
  UserOutlined,
} from '@ant-design/icons';
import Footer from './footer';
import { Redirect } from 'react-router';
import UserHome from './userHome';
import Dashboard from './dashboard';

const { Header, Content, Sider } = Layout;
const { SubMenu } = Menu;

class SideBar extends React.Component {
  state = {
    collapsed: false,
    user:true,
    load:false,
    selectedKey:'1',
  };

  onCollapse = collapsed => {
    console.log(collapsed);
    this.setState({ collapsed });
  };

  userClicked = () => {
    this.setState({
      user:true,
      selectedKey:'1'
      })

  }
  dashboardClicked = () =>{
    this.setState({
      user:false,
      selectedKey:'2',
        
        })

  }

  render() {
    let redirectPage = null;
    if (!localStorage.getItem("user_id") ) {
        redirectPage = <Redirect to="/welcome/" />
    }

    return (
        <div>
                 {redirectPage} 

        <div>
          <UserHeader />
      <Layout style={{ minHeight: '100vh' }}>
        <Sider collapsible collapsed={this.state.collapsed} onCollapse={this.onCollapse}>
          <Menu theme="dark" defaultSelectedKeys={this.state.selectedKey} mode="inline" style={{marginTop:'10%'}}>
            <Menu.Item key="1" style={{marginTop:'50%'}} onClick={this.userClicked}>
              <UserOutlined />
              <span>User</span>
            </Menu.Item>
            <Menu.Item key="2" style={{marginTop:'10%'}} onClick={this.dashboardClicked}>
              <DesktopOutlined />
              <span>Dashboard</span>
            </Menu.Item>
           
          </Menu>
        </Sider>
        <Content style={{backgroundColor:'white'}}>
          
          <div>           
            {this.state.user?<UserHome/>:
            <Dashboard />}
          </div>

          
        </Content>
      </Layout>
           </div>
      </div>
    );
  }
}

export default SideBar;