import React, { Component} from 'react';  
import {connect} from 'react-redux';  
import PropTypes from 'prop-types';
import * as userActions from '../../actions/userActions';
import UserList from './UserList';

class UserPage extends Component {  
  render() {
    return (
      <div className="col-md-12">
        <h1>Users</h1>
        <div className="col-md-4">
          <UserList users={this.props.urs} />
        </div>
      </div>
    );
  }
}


UserPage.propTypes = {
    users: PropTypes.array.isRequired
};

const mapStateToProps = state => {
  return {
    urs: state.users
  };
};


// function mapStateToProps(state, ownProps) {
//     return {
//         users: state.users
//       };
//     } 

export default connect(mapStateToProps)(UserPage);  