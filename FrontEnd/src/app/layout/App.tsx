import { observer } from "mobx-react-lite";
import WithoutOktaAuthPage from "./WithoutOktaAuthPage";
import LoginConfigJSON from "./../../loginConfig.json";
import OktaAuthPage from "./OktaAuthPage";

function App() {
  const { isOktaLoginEnabled } = LoginConfigJSON;
  return (
    <>{!isOktaLoginEnabled ? <WithoutOktaAuthPage /> : <OktaAuthPage />}</>
  );
}

export default observer(App);
