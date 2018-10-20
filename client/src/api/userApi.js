import axios from 'axios';
const API = 'http://127.0.0.1:5000/api/v1/';
const DEFAULT_QUERY = 'owner'


class UserApi {  
    static getAllUsers() {
      return axios.get(API + DEFAULT_QUERY).then(response => {
        console.log(response)
        return response.data.content;
      }).catch(error => {
        return error;
      })
      }
};
  
  export default UserApi;