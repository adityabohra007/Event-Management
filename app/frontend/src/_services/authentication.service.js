import { BehaviorSubject } from "rxjs";
import { userService } from ".";

import { handleResponse } from "./../_helpers";

const currentUserSubject = new BehaviorSubject(
  JSON.parse(localStorage.getItem("currentUser"))
);

export const authenticationService = {
  login,
  logout,
  currentUser: currentUserSubject.asObservable(),
  get currentUserValue() {
    return currentUserSubject.value;
  },
};

function login(username, password) {
  const requestOptions = {
    method: "POST",
    headers: { "Content-Type": "application/json" },
    body: JSON.stringify({ username, password }),
  };

  return fetch("http://127.0.0.1:8000/api/dj-rest-auth/login/", requestOptions)
    .then(handleResponse)
    .then(async (user) => {
      console.log(user);
      var role = await userService.getRole();
      user = { ...user, ...user.user, ...role };
      console.log(user);
      // store user details and jwt token in local storage to keep user logged in between page refreshes
      localStorage.setItem("currentUser", JSON.stringify(user));
      currentUserSubject.next(user);

      return user;
    });
}

function logout() {
  // remove user from local storage to log user out
  localStorage.removeItem("currentUser");
  currentUserSubject.next(null);
}
