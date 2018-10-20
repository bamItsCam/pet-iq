import React, {PropTypes, Component} from 'react';  
import {connect} from 'react-redux';  
import * as userActions from '../../actions/userActions';
// import CatList from './CatList';

class UserPage extends Component {  
  render() {
    return (
      <div className="col-md-12">
        <h1>Users</h1>
        <div className="col-md-4">
          {this.props.users}
        </div>
      </div>
    );
  }
}


UserPage.propTypes = {
    users: PropTypes.array.isRequired
};

function mapStateToProps(state, ownProps) {
    return {
        users: state.users
      };
    } 

export default connect(mapStateToProps)(UserPage);  