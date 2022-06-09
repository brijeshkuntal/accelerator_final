import { makeAutoObservable, reaction } from "mobx";
import { ServerError } from "../models/serverError";
import { User } from "../models/user";

export default class CommonStore {
  user: User | null = window.sessionStorage.getItem("user")
    ? JSON.parse(window.sessionStorage.getItem("user") || "")
    : null;
  error: ServerError | null = null;
  appLoaded = false;

  constructor() {
    makeAutoObservable(this);

    /*  set and remove user login details to session storage */
    reaction(
      () => this.user,
      (user) => {
        if (user) {
          window.sessionStorage.setItem("user", JSON.stringify(user));
        } else {
          window.sessionStorage.removeItem("user");
        }
      }
    );
  }

  setServerError = (error: ServerError) => {
    this.error = error;
  };

  setAppLoaded = () => {
    this.appLoaded = true;
  };

  setUser = (user: User | null) => {
    this.user = user;
  };
}
