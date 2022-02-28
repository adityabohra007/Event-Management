import React from "react";
import { Router, Route, Link } from "react-router-dom";

import { history, Role } from "./../_helpers";
import { authenticationService } from "./../_services";
import { PrivateRoute } from "./../_components";
import { HomePage } from "./../HomePage";
import { AdminPage } from "./../AdminPage";
import { LoginPage } from "./../LoginPage";
import EventDetails from "../EventDetails";
import "./index.css";
import { EventEdit } from "../EventEdit";
import { UserEventPage } from "../UserEventPage";
import UserEventDetailsPage from "../UserEventDetailsPage";
import { MyBookings } from "../MyBookings";
class App extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      currentUser: null,
      isAdmin: false,
    };
  }

  componentDidMount() {
    authenticationService.currentUser.subscribe((x) =>
      this.setState({
        currentUser: x,
        isAdmin: x && x.role === Role.Admin,
        isUser: x && x.role === Role.User,
      })
    );
  }

  logout() {
    authenticationService.logout();
    history.push("/login");
  }

  render() {
    const { currentUser, isAdmin, isUser } = this.state;
    return (
      <Router history={history}>
        <div className="mainContainer">
          <div className="navbar-wrapper">
            <div className="navbar-container">
              <div
                style={{
                  fontWeight: 600,
                  fontSize: 20,
                  padding: 20,
                  color: "#398AB9",
                }}
              >
                Event Management
              </div>
              {currentUser && (
                <nav>
                  <div style={{ display: "flex" }}>
                    <Link to="/" className="nav-link">
                      Home
                    </Link>
                    {isAdmin && (
                      <Link to="/events" className="nav-item nav-link">
                        Events
                      </Link>
                    )}
                    {isUser && (
                      <>
                        <Link to="/user/events" className="nav-item nav-link">
                          Events
                        </Link>
                        <Link to="/mybookings" className="nav-item nav-link">
                          My Booking
                        </Link>
                      </>
                    )}
                    <a onClick={this.logout} className="nav-item nav-link">
                      Logout
                    </a>
                  </div>
                </nav>
              )}
            </div>
          </div>
          <div>
            <div>
              <div>
                <div>
                  <PrivateRoute exact path="/" component={HomePage} />

                  <PrivateRoute
                    path="/events"
                    roles={[Role.Admin]}
                    component={AdminPage}
                  />
                  <PrivateRoute
                    exact={true}
                    path="/event/:id/edit/"
                    roles={[Role.Admin]}
                    component={EventEdit}
                  />
                  <PrivateRoute
                    exact={true}
                    path="/event/:id"
                    roles={[Role.Admin]}
                    component={EventDetails}
                  />

                  <PrivateRoute
                    exact={true}
                    path="/mybookings"
                    roles={[Role.User]}
                    component={MyBookings}
                  />

                  <PrivateRoute
                    path="/user/events"
                    roles={[Role.User]}
                    component={UserEventPage}
                  />

                  <PrivateRoute
                    exact={true}
                    path="/user/event/:id"
                    roles={[Role.User]}
                    component={UserEventDetailsPage}
                  />
                  {/* <PrivateRoute
                    exact={true}
                    path="user/event/:id"
                    roles={[Role.User]}
                    component={EventDetails}
                  /> */}

                  <Route path="/login" component={LoginPage} />
                </div>
              </div>
            </div>
          </div>
        </div>
      </Router>
    );
  }
}

export { App };
