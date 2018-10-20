import userApi from '../api/userApi';
import * as types from './actionTypes';  

export function loadUsersSuccess(cats) {  
  return {type: types.LOAD_USERS_SUCCESS, cats};
}

export function loadUsers() {  
  return function(dispatch) {
    return userApi.getAllUsers().then(user => {
      dispatch(loadUsersSuccess(user));
    }).catch(error => {
      throw(error);
    });
  };
}

