import React, { Component } from "react";
import axios from "axios";
import { render } from "react-dom";
//import HomePage from "./HomePage";

export default class Welcome extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <h1>Welcome, </h1>
    );
  }
}

const appDiv = document.getElementById("welcome");
render(<Welcome />, appDiv);