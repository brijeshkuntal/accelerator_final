import { observer } from "mobx-react-lite";
import { useEffect, useState } from "react";
import { Link } from "react-router-dom";
import { Container, Header, Segment, Image, Button } from "semantic-ui-react";
import { useStore } from "../../app/stores/store";
import LoginForm from "../users/LoginForm";
import RegisterForm from "../users/RegisterForm";
import { withOktaAuth } from "@okta/okta-react";
import AppConfigJSON from "./../../appConfig.json";

export default observer(
  withOktaAuth(function HomePage(props) {
    const { userStore, modalStore } = useStore();
    const [isLoggedIn, setIsLoggedIn] = useState<boolean>(false);
    const { isOktaLoginEnabled } = AppConfigJSON;
    const { authState, oktaAuth } = props;

    const login = async () => {
      await oktaAuth.signInWithRedirect();
    };

    useEffect(() => {
      if (isOktaLoginEnabled) {
        setIsLoggedIn(authState?.isAuthenticated || false);
      } else {
        setIsLoggedIn(userStore.isLoggedIn);
      }
    }, [authState, userStore.isLoggedIn, isOktaLoginEnabled]);

    return (
      <Segment inverted textAlign="center" vertical className="masthead">
        <Container text>
          <Header as="h1" inverted>
            <Image
              size="massive"
              src="/assets/logo.png"
              alt="logo"
              style={{ marginBottom: 12 }}
            />
            Demo Project
          </Header>
          {isLoggedIn ? (
            <>
              <Button as={Link} to="/employee" size="huge" inverted>
                Manage Employee
              </Button>
            </>
          ) : (
            <>
              <Button
                onClick={() => {
                  !isOktaLoginEnabled
                    ? modalStore.openModal(<LoginForm />)
                    : login();
                }}
                size="huge"
                inverted
              >
                Login!
              </Button>
              <Button
                onClick={() => modalStore.openModal(<RegisterForm />)}
                size="huge"
                inverted
              >
                Register!
              </Button>
            </>
          )}
        </Container>
      </Segment>
    );
  })
);
