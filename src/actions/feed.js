import axios from 'axios';
import {GET_FEED_DATA,FEED_FETCH_ERROR} from './types';

export const getAllFeeds = () => async dispatch =>{
    try{
        const feeds = await axios.get(`${process.env.REACT_APP_API_URL}/api/feeds`);
        console.log("Here")
        console.log("Feeds",feeds)
        dispatch({
            type: GET_FEED_DATA,
            payload: feeds.data
        })
    }
    catch(err){
        dispatch({
            type: FEED_FETCH_ERROR,
            payload: err
        })

    }
}