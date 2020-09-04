import React from 'react';
import './SingleFeed.css'

const SingleFeed = ({creator, content, image,likeCount}) =>{
    return(
        <div className="profile-feed">
        <div className="d-flex align-items-start profile-feed-item">
          <div className="ml-4">
            <b>
              {creator}
              {/* <small className="ml-4 text-muted"><i className="mdi mdi-clock mr-1"></i>10 hours</small> */}
            </b>
            <p>
            <div dangerouslySetInnerHTML={{__html: content}} />
              {/* {content} */}
            </p>
            {/* <img 
            src="https://images.unsplash.com/photo-1583912267550-d974311a9a6e?ixlib=rb-1.2.1&ixid=eyJhcHBfaWQiOjEyMDd9&auto=format&fit=crop&w=1350&q=80" 
            alt="depressed"
            width="400" height="400"
            /> */}
            <p className="small text-muted mt-2 mb-0">
              <span>
                <i className="mdi mdi-thumb-up mr-1"></i>{likeCount}
              </span>
              <span className="ml-2">
                <i className="mdi mdi-reply"></i>
              </span>
            </p>
          </div>
        </div>
        </div>

    )
}

export default SingleFeed