import { makeAutoObservable, runInAction } from "mobx";
import { history } from "../..";
import agent from "../api/agent";
import { User, UserFormValues } from "../models/user";
import { store } from "./store";

export default class UserStore {
  user: User | null = null;

  constructor() {
    makeAutoObservable(this);
  }

  /* returns user details after login */
  get isLoggedIn() {
    return !!store.commonStore.user;
  }

  /* function to login the user */
  login = async (creds: UserFormValues) => {
    try {
      const user = await agent.Account.login(creds);
      store.commonStore.setUser(user);
      runInAction(() => (this.user = user));
      history.push("/employee");
      store.modalStore.closeModal();
    } catch (error) {
      throw error;
    }
  };

  /* function to logout the user */
  logout = () => {
    store.commonStore.setUser(null);
    this.user = null;
    window.location.href = "/";
  };

  /* function to register the user */
  register = async (creds: UserFormValues) => {
    try {
      const user = await agent.Account.register(creds);
      store.commonStore.setUser(user);
      runInAction(() => (this.user = user));
      history.push("/employee");
      store.modalStore.closeModal();
    } catch (error) {
      throw error;
    }
  };
}
