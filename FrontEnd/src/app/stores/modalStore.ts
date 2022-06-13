import { makeAutoObservable } from "mobx";

interface Modal {
  open: boolean;
  body: JSX.Element | null;
}

export default class ModalStore {
  modal: Modal = {
    open: false,
    body: null,
  };

  constructor() {
    makeAutoObservable(this);
  }

  openModal = (content: JSX.Element) => {
    this.setModal({ open: true, body: content });
  };

  closeModal = () => {
    this.setModal({ open: false, body: null });
  };

  setModal = (modal: Modal) => {
    this.modal = modal;
  };
}
