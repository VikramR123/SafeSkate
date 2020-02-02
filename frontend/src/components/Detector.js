import React, { Component } from 'react';
import * as firebase from 'firebase';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExclamationTriangle } from '@fortawesome/free-solid-svg-icons';

class Detector extends Component {

    constructor(props) {
        super(props);
        this.state = {
            'detected' : 0,
            'firebase' : firebase.initializeApp({
                'databaseURL': 'https://safeskate-499c0.firebaseio.com/'
            })
        };
    }

    componentDidMount() {
        let ref = this.state.firebase.database().ref("safeskate-499c0/obs_table");
        ref.once("value").then(snap => {
            this.setState((state, props) => ({ 
                detected: 0 
            }));
            console.log(this.state.detected);
        }).catch(error => {
            console.log("error".error);
        })

        setInterval(() => this.tick(), 1000);
    }

    tick() {
        let ref = this.state.firebase.database().ref("safeskate-499c0/obs_table");
        ref.once("value").then(snap => {
            this.setState((state, props) => ({ 
                detected: snap.val().obstruction 
            }));
            console.log(this.state.detected);
        }).catch(error => {
            console.log("error".error);
        })
    }

    render() {
        let detectedMessage = 
            !this.state.detected ? "No obstruction detected." 
            : "Obstruction detected!"

        let image = 
            !this.state.detected ? <FontAwesomeIcon className="detectorImg nodanger" icon={faExclamationTriangle}/>
            : <FontAwesomeIcon className="detectorImg danger" icon={faExclamationTriangle}/>

        return (
            <div className="detector">
                {image}
                <h3>{detectedMessage}</h3>
            </div>
        )
    }
}

export default Detector;