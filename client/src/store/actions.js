import axios from 'axios';
const API = 'http://127.0.0.1:5000/api/v1/';
const DEFAULT_QUERY = 'owner'

export const GET_USERS = 'GET_USERS'

export const getUsers = () => {
    return dispatch => {
        
    }
    return {
        type: GET_USERS
    };
};