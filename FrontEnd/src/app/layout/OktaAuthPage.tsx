import { OktaAuth, toRelativeUrl } from "@okta/okta-auth-js";
import { LoginCallback, Security, SecureRoute } from "@okta/okta-react";
import { Route, Switch, useHistory, useLocation } from "react-router-dom";
import { Container } from "semantic-ui-react";
import EmpDashboard from "../../features/employees/dashboard/EmpDashboard";
import EmpDelete from "../../features/employees/details/EmpDelete";
import EmpDetails from "../../features/employees/details/EmpDetails";
import EmpForm from "../../features/employees/form/EmpForm";
import NotFound from "../../features/errors/NotFound";
import HomePage from "../../features/home/HomePage";
import { useStore } from "../stores/store";
import NavBar from "./NavBar";

interface Props {}

const oktaAuth = new OktaAuth({
  issuer: `https://${process.env.REACT_APP_OKTA_DOMAIN}/oauth2/default`,
  clientId: process.env.REACT_APP_OKTA_CLIENT_ID,
  redirectUri: window.location.origin + "/login/callback",
});

function OktaAuthPage(props: Props) {
  const location = useLocation();
  const { commonStore, userStore } = useStore();
  const history = useHistory();

  const restoreOriginalUri = async (_oktaAuth: OktaAuth, originalUri: any) => {
    history.replace(toRelativeUrl(originalUri || "/", window.location.origin));
  };

  return (
    <Security oktaAuth={oktaAuth} restoreOriginalUri={restoreOriginalUri}>
      <Route exact path="/" component={HomePage} />
      <Route path="/login/callback" component={LoginCallback} />
      <SecureRoute
        path={"/(.+)"}
        render={() => (
          <>
            <NavBar />
            <Container style={{ marginTop: "7em" }}>
              <Switch>
                <Route exact path="/employee" component={EmpDashboard} />
                <Route path="/employee/:id" component={EmpDetails} />
                <Route
                  key={location.key}
                  path={["/createEmployee", "/manage/:id"]}
                  component={EmpForm}
                />
                <Route path="/empdel/:id" component={EmpDelete} />
                {/* <Route path="/login" component={LoginForm} /> */}
                <Route component={NotFound} />
              </Switch>
            </Container>
          </>
        )}
      />
    </Security>
  );
}

export default OktaAuthPage;
