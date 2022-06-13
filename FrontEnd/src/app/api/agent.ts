import axios, { AxiosError, AxiosResponse } from "axios";
import jwtDecode from "jwt-decode";
import { toast } from "react-toastify";
import { history } from "../..";
import { sleep } from "../common/utils/common";
import { Employee } from "../models/employee";
import { User, UserFormValues } from "../models/user";
import { store } from "../stores/store";
import LoginConfigJSON from "./../../loginConfig.json";

/* base url for the api requests */
const baseUrl = "http://nagarro.test.com:8000";

const axiosInstance = axios.create({
  baseURL: baseUrl,
});

/*request interceptor method => to be run before sending each api request*/
axiosInstance.interceptors.request.use(async (config: any) => {
  if (!LoginConfigJSON.isOktaLoginEnabled) {
    const user = store.commonStore.user;
    if (user) {
      let { access, refresh } = user;

      const decodeJWT: any = jwtDecode(access);

      /* checking expired jwt token.
     if expired, getting new jwt token  */
      if (new Date() > new Date(decodeJWT.exp * 1000)) {
        const refreshResponse = await axios.post(
          `${baseUrl}/api/token/refresh/`,
          { refresh }
        );
        access = refreshResponse.data.access;
        store.commonStore.setUser({ ...user, access });
      }

      /* adding jwt token to the request headers */
      config.headers.Authorization = `Bearer ${access}`;
    }
  } else {
    /* const oktaTokenStorage: any = JSON.parse(
      localStorage.getItem("okta-token-storage") || ""
    );
    if (oktaTokenStorage.accessToken) 
      config.headers.Authorization = `Bearer ${oktaTokenStorage.accessToken.accessToken}`; */
  }
  return config;
});

/*response interceptor method => to run after each api response*/
axiosInstance.interceptors.response.use(
  async (response) => {
    await sleep(1000);
    return response;
  },
  async (error: AxiosError) => {
    const { data, status, config }: AxiosResponse = error.response!;
    switch (status) {
      case 400:
        if (config.method === "get" && data.errors.hasOwnProperty("id")) {
          history.push("/not-found");
        }
        if (data.errors) {
          const modalStateErrors = [];
          for (const key in data.errors) {
            if (data.errors[key]) {
              modalStateErrors.push(data.errors[key]);
            }
          }
          throw modalStateErrors.flat();
        } else {
          toast.error(data);
        }
        break;
      case 401:
        toast.error("unauthorised.please relogin");
        store.userStore.logout();
        break;
      case 404:
        history.push("/not-found");
        break;
      case 500:
        history.push("/server-error");
        break;
    }
    return Promise.reject(error);
  }
);

/* returns response of the api */
const responseBody = <T>(response: AxiosResponse<T>) => response.data;

/* instances for api crud operations */
const requests = {
  get: <T>(url: string) => axiosInstance.get<T>(url).then(responseBody),
  post: <T>(url: string, body: {}) =>
    axiosInstance.post<T>(url, body).then(responseBody),
  put: <T>(url: string, body: {}) =>
    axiosInstance.put<T>(url, body).then(responseBody),
  del: <T>(url: string) => axiosInstance.delete<T>(url).then(responseBody),
};

/* api for employee crud operations */
const Employees = {
  list: () => requests.get<Employee[]>("/employees/"),
  details: (id: number) => requests.get<Employee>(`/employee/${id}/`),
  create: (employee: Employee) =>
    requests.post<void>("/create_employee/", employee),
  update: (employee: Employee) =>
    requests.put<void>(`/employee/${employee.empID}/`, employee),
  delete: (id: number) => requests.del<void>(`/employee/${id}/`),
};

/* api for user login and register */
const Account = {
  login: (user: UserFormValues) => requests.post<User>("/user_login/", user),
  register: (user: UserFormValues) =>
    requests.post<User>("/register_user/", user),
};

const agent = {
  Employees,
  Account,
};

export default agent;
