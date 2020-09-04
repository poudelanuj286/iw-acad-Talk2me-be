import {GET_FEED_DATA} from '../actions/types';

const initialState = {
    feedData:{}
}

export default function (state = initialState, action) {
    switch (action.type) {
        case GET_FEED_DATA:
            return {
                ...state,
                feedData: action.payload
            };
        default:
            return state;
    }
}