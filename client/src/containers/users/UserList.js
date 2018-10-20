import React, {PropTypes} from 'react';

const UserList = ({users}) => {  
  return (
      <ul className="list-group">
        {users.map(users => 
          <li className="list-group-item" key={users.id}>
            {users.name}
          </li>
        )}
      </ul>
  );
};

// UserList.propTypes = {  
//     users: PropTypes.array.isRequired
// };

export default UserList;  