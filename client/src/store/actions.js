import axios from 'axios';
import * as types from './actionTypes';  
import userApi from '../api/userApi';

export const GET_USERS = 'GET_USERS'
export const GET_USERS_START = 'GET_USERS_START'
export const LOAD_USERS_SUCCESS = 'LOAD_CATS_SUCCESS'; 

export function loadUsersSuccess(users) {  
    return {type: types.LOAD_USERS_SUCCESS, users};
  }

// export const getUsers = () => {
//     axios.get(API + DEFAULT_QUERY)
//     return dispatch => {
//         type: GET_USERS_START
//     }
//     return {
//         type: GET_USERS
//     };
// };

export function getUsers() {  
    return function(dispatch) {
      return axios.get(API + DEFAULT_QUERY).then(users => {
        dispatch(loadUsersSuccess(users));
      }).catch(error => {
        throw(error);
      });
    };
  }