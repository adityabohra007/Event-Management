import React from "react";
import {
  StyledPage,
  StyledSection,
  StyledTitle,
} from "../_components/StyledPage";

import { userService, authenticationService } from "./../_services";

class HomePage extends React.Component {
  constructor(props) {
    super(props);

    this.state = {
      currentUser: authenticationService.currentUserValue,
      userFromApi: null,
    };
  }

//   componentDidMount() {
//     const { currentUser } = this.state;
//     userService
//       .getById(currentUser.id)
//       .then((userFromApi) => this.setState({ userFromApi }));
//   }

  render() {
    const { currentUser, userFromApi } = this.state;
    return (
      <StyledPage>
        <StyledSection>
          <StyledTitle>Home Page</StyledTitle>
        </StyledSection>
      </StyledPage>
    );
  }
}

export { HomePage };
