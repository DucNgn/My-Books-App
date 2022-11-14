/*
The book project lets a user keep track of different books they would like to read, are currently
reading, have read or did not finish.
Copyright (C) 2021  Karan Kumar

This program is free software: you can redistribute it and/or modify it under the terms of the
GNU General Public License as published by the Free Software Foundation, either version 3 of the
License, or (at your option) any later version.

This program is distributed in the hope that it will be useful, but WITHOUT ANY
WARRANTY; without even the implied warranty of MERCHANTABILITY or FITNESS FOR A PARTICULAR
PURPOSE.  See the GNU General Public License for more details.

You should have received a copy of the GNU General Public License along with this program.
If not, see <https://www.gnu.org/licenses/>.
*/

import Verb from "./verb";
import Endpoints from "../api/endpoints";
import {
  ApolloClient as ApolloClientBase,
  InMemoryCache,
} from "@apollo/client";

// eslint-disable-next-line @typescript-eslint/naming-convention
let HttpClient: () => HttpClientBase;
(function() {
  // Creating a singleton instance of an HTTP client
  let instance: HttpClientBase;
  HttpClient = function HttpClient(): HttpClientBase {
    if (instance !== undefined) {
      return instance;
    }
    instance = new HttpClientBase();
    return instance;
  }
})();

// eslint-disable-next-line @typescript-eslint/no-explicit-any
type HttpReponse = Promise<Record<string, any>>

// Base class for managing HTTP requests
class HttpClientBase {
  baseUrl = 'http://localhost:8000/api/v1/';
  mode: "cors" | "navigate" | "no-cors" | "same-origin" | undefined = "cors";
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  headers: any = {
    // eslint-disable-next-line @typescript-eslint/naming-convention
    "Authorization": null,
    // eslint-disable-next-line @typescript-eslint/naming-convention
    "Content-Type": "application/json",
    // eslint-disable-next-line @typescript-eslint/naming-convention
    "Access-Control-Allow-Origin": "*",
  };
  // eslint-disable-next-line @typescript-eslint/no-explicit-any
  get(url: string): any {
    if (this.headers["Authorization"] === null) {
      window.location.replace("http://localhost:3000/sign-in");
    }
    const requestOptions = {
      method: Verb.GET,
      headers: this.headers,
    };
    return fetch(url, requestOptions)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      });
  }

  post(url: string, param: string): Promise<Response> {
    if (this.headers["Authorization"] === null) {
      window.location.replace("http://localhost:3000/sign-in");
    }
    const requestOptions = {
      method: Verb.POST,
      headers: this.headers,
    };
    return fetch(url + "/" + param, requestOptions)
      .then(response => {
        if (response.ok) {
          return response.json();
        }
        throw response;
      });
  }

  getHeaders() {
    if (this.headers["Authorization"] === null) {
      window.location.replace("http://localhost:3000/sign-in");
    } else {
      return this.headers;
    }
  }

  login(email: string, password: string): HttpReponse {
    console.log(email)
    console.log(password)
    const currentHeaders = new Headers();
    currentHeaders.append('accept', 'application/json');
    currentHeaders.append('Content-Type', 'application/x-www-form-urlencoded');
    currentHeaders.append("Access-Control-Allow-Origin", "*");

    const formData = new FormData();
    formData.append('username', email);
    formData.append('password', password);

    const requestOptions = {
      url: this.baseUrl,
      method: Verb.POST,
      mode: this.mode,
      headers: currentHeaders,
      data: formData,
    };

    return fetch(this.baseUrl + Endpoints.login, requestOptions)
      .then(response => {
        console.log(response);
        const headers = response.headers;
        this.headers['Authorization'] = headers.get('Authorization');
        return response;
      });
  }

  deleteAccount(password: string): HttpReponse {
    const mode: 'cors' | undefined = 'cors';
    const requestOptions = {
      method: Verb.DELETE,
      mode: mode,
      headers: this.headers,
      body: JSON.stringify({
        password: password
      })
    };
    return fetch(this.baseUrl + Endpoints.user, requestOptions)
      .then(response => {
        if (response.ok) {
          this.headers['Authorization'] = null;
        }
        return response;
      });
  }
}

const httpClientInstance = HttpClient();
export const apolloClient = new ApolloClientBase({
  uri: 'http://localhost:8082/graphql',
  cache: new InMemoryCache(),
  headers: httpClientInstance.headers
});

export default httpClientInstance;

