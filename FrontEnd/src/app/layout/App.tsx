import { observer } from "mobx-react-lite";
import WithoutOktaAuthPage from "./WithoutOktaAuthPage";
import AppConfigJSON from "./../../appConfig.json";
import OktaAuthPage from "./OktaAuthPage";
import { ToastContainer } from "react-toastify";
import ModalContainer from "../common/modals/ModalContainer";

function App() {
  const { isOktaLoginEnabled } = AppConfigJSON;
  return (
    <>
      <ToastContainer position="bottom-right" hideProgressBar />
      <ModalContainer />
      {!isOktaLoginEnabled ? <WithoutOktaAuthPage /> : <OktaAuthPage />}
    </>
  );
}

export default observer(App);
