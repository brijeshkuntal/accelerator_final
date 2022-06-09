export interface User {
  username: string;
  displayName: string;
  refresh: string;
  access: string;
}

export interface UserFormValues {
  email: string;
  password: string;
  displayName?: string;
  username?: string;
}

export interface VerifyToken {
  token: string;
}
export interface GetAccessToken {
  refresh: string;
}
