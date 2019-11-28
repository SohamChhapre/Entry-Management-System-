import React from 'react';
import {Link} from 'react-router-dom';
import './style.css';
const Home=()=>{
    return (    <div>
        <div className="bg-color">
            Welcome to Entry Management System
        </div>
        <div>
            
            <Link to="/visitor" type="button" className="btn btn-outline-primary pd btn-lg">Visitor</Link>
        <Link to="/host" className="btn btn-outline-primary pd btn-lg">Host</Link>
        </div>
    </div>  );
};

export default Home;
