import * as actionTypes from './actions'

const initialState = {
    users: [],
    isLoading: false,
    error: null
    
}

const reducer = (state = initialState, acition) =>{
    switch (action.type) {
        case actionTypes.GET_USERS:
        return {

        }
        
    }
    return state
}

export default reducer