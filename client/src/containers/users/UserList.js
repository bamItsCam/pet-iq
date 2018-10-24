import React from 'react';
import PropTypes from 'prop-types';

const UserList = ({users}) => {  
  return (
      <ul className="list-group">
        {users.map(users => 
          <li className="list-group-item" key={users.id}>
            {users.email}
          </li>
        )}
      </ul>
  );
};

UserList.propTypes = {  
    users: PropTypes.array.isRequired
};

export default UserList;  