import React from 'react';
import { Route } from 'react-router-dom';
import WelcomePage from './welcomePage';
import LoginForm from './login';
import RegistrationForm from './joinus';
import UserHome from './sidebar';
//import UserProfile from './userProfile';

// Main Component
class Main extends React.Component {
  render() {
    return (
      <div>
        {/* Render Different Component based on Route */}
        <Route exact path="/" component={WelcomePage} />
        <Route path="/welcome/" component={WelcomePage} />
        <Route path="/signin/" component={LoginForm} />
        <Route path="/joinus/" component={RegistrationForm} />
        {/* <Route path="/user/dashboard/" component={UserHome} /> */}
        <Route path="/user/home/" component={UserHome} />


        {/* <Route path="/user/profile/" component={UserProfile} /> */}

      </div>
    );
  }
}

// Export The Main Component
export default Main;
