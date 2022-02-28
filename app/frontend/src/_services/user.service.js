import { authHeader, handleResponse } from "./../_helpers";

export const userService = {
  getAll,
  getById,
  getRole,
};

function getAll() {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch(`http://127.0.0.1:8000/users`, requestOptions).then(
    handleResponse
  );
}

function getById(id) {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch(`http://127.0.0.1:8000/users/${id}`, requestOptions).then(
    handleResponse
  );
}

function getRole(id) {
  const requestOptions = { method: "GET", headers: authHeader() };
  return fetch("http://127.0.0.1:8000/api/user/role", requestOptions).then(
    handleResponse
  );
}
