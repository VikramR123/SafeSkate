import React, { Component } from 'react';
import * as firebase from 'firebase';
import { FontAwesomeIcon } from '@fortawesome/react-fontawesome';
import { faExclamationCircle, faCheckCircle } from '@fortawesome/free-solid-svg-icons';
import ReactHowler from 'react-howler';

class Detector extends Component {

    constructor(props) {
        super(props);
        this.state = {
            'detected' : 0,
            'firebase' : firebase.initializeApp({
                'databaseURL': 'https://safeskate-499c0.firebaseio.com/'
            }),
        };
        
    }

    componentDidMount() {
        let ref = this.state.firebase.database().ref("safeskate-499c0/obs_table");
        ref.once("value").then(snap => {
            this.setState((state, props) => ({ 
                detected: snap.val().obstruction
            }));
            console.log(this.state.detected);
        }).catch(error => {
            console.log("error".error);
        })
        setInterval(() => this.tick(), 200);
    }

    tick() {
        let ref = this.state.firebase.database().ref("safeskate-499c0/obs_table");
        
        if (this.state.detected) {

        }

        ref.once("value").then(snap => {
            this.setState((state, props) => ({ 
                detected: snap.val().obstruction
            }));
            console.log(this.state.detected);
        }).catch(error => {
            console.log("error".error);
        });

    }

    render() {
        let detectedMessage = 
            !this.state.detected ? "No obstruction detected." 
            : "Obstruction detected!"

        let image = 
            !this.state.detected ? <FontAwesomeIcon className="detectorImg nodanger" icon={faCheckCircle}/>
            : <FontAwesomeIcon className="detectorImg danger" icon={faExclamationCircle}/>

        return (
            <React.Fragment>
                <ReactHowler
                    src='../beep1.mp3'
                    playing={true}
                    loop ={true}
                />
                <div className="detector">
                    {image}
                    <h3>{detectedMessage}</h3>
                </div>
            </React.Fragment>
            
        )
    }
}

export default Detector;