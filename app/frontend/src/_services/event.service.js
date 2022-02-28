import { authHeader, handleResponse } from "../_helpers";

export const eventService = {
  getEvents,
  getEventDetails,
  postEventEdit,
  getUserEvents,
  getUserEventDetails,
  postEventRegistration,
  getEventBookings,
  getUserBookings,
};

function getEvents() {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch("http://127.0.0.1:8000/api/events/", requestOptions).then(
    handleResponse
  );
}

function getEventDetails(id) {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch("http://127.0.0.1:8000/api/events/" + id, requestOptions).then(
    handleResponse
  );
}

function postEventEdit(id, data) {
  const auth = authHeader();
  console.log(data);
  const headers = { ...auth, "Content-Type": "application/json" };
  const requestOptions = {
    method: "PATCH",
    body: JSON.stringify(data),
    headers: headers,
  };
  return fetch(
    "http://127.0.0.1:8000/api/events/" + id + "/",
    requestOptions
  ).then(handleResponse);
}

function getUserEvents() {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch("http://127.0.0.1:8000/api/user/events/", requestOptions).then(
    handleResponse
  );
}

function getUserEventDetails(id) {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch(
    "http://127.0.0.1:8000/api/user/events/" + id,
    requestOptions
  ).then(handleResponse);
}

function postEventRegistration(id) {
  const auth = authHeader();
  const headers = { ...auth, "Content-Type": "application/json" };
  const requestOptions = {
    method: "POST",
    headers,
    body: JSON.stringify({ event: parseInt(id) }),
  };
  return fetch(
    "http://127.0.0.1:8000/api/user/event/registration",
    requestOptions
  ).then(handleResponse);
}

function getEventBookings(id) {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch(
    "http://127.0.0.1:8000/api/events/" + id + "/bookings",
    requestOptions
  ).then(handleResponse);
}

function getUserBookings() {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch("http://127.0.0.1:8000/api/mybookings", requestOptions).then(
    handleResponse
  );
}
