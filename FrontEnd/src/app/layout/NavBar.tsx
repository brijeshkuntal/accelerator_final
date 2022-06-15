import { observer } from "mobx-react-lite";
import { NavLink } from "react-router-dom";
import { Button, Container, Menu, Dropdown } from "semantic-ui-react";
import { useStore } from "../stores/store";
import { withOktaAuth } from "@okta/okta-react";
import AppConfigJSON from "./../../appConfig.json";
import { useEffect, useState } from "react";

export default observer(
  withOktaAuth(function NavBar(props) {
    const { isOktaLoginEnabled } = AppConfigJSON;
    const [displayName, setDisplayName] = useState<string>();
    const { authState, oktaAuth } = props;

    const {
      userStore: { logout },
      commonStore,
    } = useStore();

    const logoutUser = async () => {
      await oktaAuth.signOut();
    };

    useEffect(() => {
      if (isOktaLoginEnabled && authState?.isAuthenticated) {
        oktaAuth.getUser().then((info) => setDisplayName(info.name));
      } else {
        setDisplayName(commonStore.user?.displayName);
      }
    }, [commonStore.user, oktaAuth, authState]);

    return (
      <Menu inverted fixed="top">
        <Container>
          <Menu.Item as={NavLink} exact to="/" header>
            <img
              src="/assets/logo.png"
              alt="logo"
              style={{ marginRight: "10px" }}
            />
            Employees
          </Menu.Item>
          <Menu.Item as={NavLink} to="/employee" name="Employees" />
          <Menu.Item>
            <Button
              as={NavLink}
              to="/createEmployee"
              positive
              content="Create Employee"
            />
          </Menu.Item>
          <Menu.Item position="right">
            <Dropdown pointing="top left" text={displayName}>
              <Dropdown.Menu>
                <Dropdown.Item
                  onClick={!isOktaLoginEnabled ? logout : logoutUser}
                  text="Logout"
                  icon="power"
                />
              </Dropdown.Menu>
            </Dropdown>
          </Menu.Item>
        </Container>
      </Menu>
    );
  })
);
