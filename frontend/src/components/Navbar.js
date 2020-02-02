import React, { Component } from 'react';
import logo from '../logo.png';

class Navbar extends Component {
    render() {
        return (
            <nav className="navbar navbar-expand-md navbar-light bg-light">
            <img className="navbar-brand logo" src={logo} alt=""/>
            <button className="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarSupportedContent" aria-controls="navbarSupportedContent" aria-expanded="false" aria-label="Toggle navigation">
                <span className="navbar-toggler-icon"></span>
            </button>
            <ul className="collapse navbar-collapse navbar-nav" id="navbarSupportedContent">
                <li className="nav-link">Devpost</li>
                <li className="nav-link">Github</li>
            </ul>
            </nav>
        )
    }
}

export default Navbar;