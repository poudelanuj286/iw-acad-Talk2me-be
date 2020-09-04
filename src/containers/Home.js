import React, { useEffect, useState } from 'react';
import { connect } from 'react-redux';
import Axios from 'axios';
import { Redirect } from 'react-router-dom';
import { getAllFeeds } from '../actions/feed';
import SingleFeed from './SingleFeed';
//import { Link } from 'react-router-dom';

const Home = (props) => {
    const [feeds, setFeeds] = useState([])
    const [content, setContents] = useState("")
    useEffect(() => {
        async function getFeeds() {
            const feeds = await Axios.get(`${process.env.REACT_APP_API_URL}/api/feeds`)
            setFeeds(feeds.data)
        }
        getFeeds()
    }, [])
    // [feeds] To update content instantly but it call api not-stop
    if (!props.isAuthenticated) {
        return <Redirect className="btn btn-primary btn-lg" to='/login' role="button">Login</Redirect>
    }

    function onContentChange(e) {
        e.preventDefault();
        setContents(e.target.value);
    }

    async function handleSubmit(e) {
        e.preventDefault();
        const config = {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded;charset=UTF-8'
            }
        };
        const data = new URLSearchParams();
        data.append('content', content)
        const me = JSON.parse(localStorage.getItem('me'))
        feeds.push({ id: me.id, content, name: me.name })
        await Axios.post(`${process.env.REACT_APP_API_URL}/api/feeds/create/`, data, config)

    }

    return (
        <div className='container'>
            <div className='row text-center'>
                <div className='col'>
                    <h1>Welcome to Talk2me </h1>
                </div>
            </div>

            <div className='row mb-3'>
                <div className='col-md-4 mx-auto col-10'>
                    <form className='form' id='feed-create-form' onSubmit={handleSubmit}>
                        {/* {% csrf_token %} */}
                        <div className='d-none alert alert-danger' id='feed-create-form-error'></div>
                        <input
                            type='hidden'
                            value='/'
                            name='next'
                        />
                        <textarea
                            required='required'
                            className='form-control rounded-0'
                            rows="8"
                            onChange={onContentChange}
                            name='content'
                            placeholder='how are you feeling...'
                        ></textarea>
                        <input type="file" name="file" />
                        <button type='submit' className='btn btn-primary'>Post</button>
                    </form>
                </div>
            </div>

            {feeds.map((item, index) => {
                return <SingleFeed
                    creator={item.name}
                    content={item.content}
                    likeCount={item.likes}
                    // image={item.image}
                    key={index}
                />
            })}


        </div>



    );
}

const mapStateToProps = state => ({
    isAuthenticated: state.auth.isAuthenticated,
    feedData: state.feed.feedData
});

export default connect(mapStateToProps, { getAllFeeds })(Home);

