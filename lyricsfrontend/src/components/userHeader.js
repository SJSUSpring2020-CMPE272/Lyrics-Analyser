import React, { Component } from 'react';
import { Menu} from 'antd';
import { Redirect } from 'react-router';


class UserHeader extends Component{

    constructor(props) {
        super(props);
        this.state = {
          redirectPage:''
        };
      }
  

  clickedLogout = () => {
    localStorage.clear();
    this.setState({
      redirectPage: <Redirect to = {{pathname:'/welcome/'}} />
    }) 
  }


render(){
return ( 

    <div>
        {this.state.redirectPage}
        <div style={{background:'grey'}}>
  
    <Menu
    theme="dark"
    mode="horizontal"
      defaultSelectedKeys={this.props.selectedKey}
      style={{  fontWeight:'bold' }}
    >

      <Menu.Item key="2" onClick={this.clickedLogout} style={{color:'white', float:'right'}}>Logout</Menu.Item>
     
    </Menu>
  
  </div>
  
  </div>
  
  )
}



}

export default UserHeader;