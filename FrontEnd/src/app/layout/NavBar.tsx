import { observer } from "mobx-react-lite";
import { NavLink } from "react-router-dom";
import { Button, Container, Menu, Dropdown } from "semantic-ui-react";
import { useStore } from "../stores/store";
import { withOktaAuth } from "@okta/okta-react";
import LoginConfigJSON from "./../../loginConfig.json";
import { useEffect, useState } from "react";

export default observer(
  withOktaAuth(function NavBar(props) {
    const { isOktaLoginEnabled } = LoginConfigJSON;
    const [displayName, setDisplayName] = useState<string>();

    const {
      userStore: { user, logout },
      commonStore,
    } = useStore();

    const logoutUser = async () => {
      await props.oktaAuth.signOut();
    };

    useEffect(() => {
      if (isOktaLoginEnabled) {
        props.oktaAuth.getUser().then((info) => setDisplayName(info.name));
      } else {
        setDisplayName(commonStore.user?.displayName);
      }
    }, [commonStore.user, props.oktaAuth]);

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
            <Dropdown
              pointing="top left"
              text={/* commonStore.user?.displayName */ displayName}
            >
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
