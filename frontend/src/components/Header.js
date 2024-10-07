import React, { Component } from "react";
import axios from "axios";
import { render } from "react-dom";
//import HomePage from "./HomePage";

export default class Header extends Component {
  constructor(props) {
    super(props);
  }

  render() {
    return (
        <div className="col-md-3 mb-2 mb-md-0">
            <a href="/" className="d-inline-flex link-body-emphasis text-decoration-none">
                <svg className="bi" width="40" height="32" role="img" aria-label="Bootstrap">
                    {/*<use xlink:href="#bootstrap"></use>*/}
                </svg>
            </a>
        </div>
  );
  }
}

const appDiv = document.getElementById("header_element");
render(<Header/>, appDiv);