import { ErrorMessage, Form, Formik } from "formik";
import { observer } from "mobx-react-lite";
import { Button, Header, Label } from "semantic-ui-react";
import MyTextInput from "../../app/common/form/MyTextInput";
import { useStore } from "../../app/stores/store";
import * as Yup from "yup";

export default observer(function LoginForm() {
  const { userStore } = useStore();
  return (
    <Formik
      initialValues={{ email: "", password: "", error: null }}
      onSubmit={(values, { setErrors, setSubmitting }) => {
        userStore
          .login(values)
          .catch((error) => setErrors({ error: "Invalid email or password" }))
          .finally(() => setSubmitting(false));
      }}
      validationSchema={Yup.object({
        username: Yup.string().required(),
        password: Yup.string().required(),
      })}
    >
      {({ handleSubmit, isSubmitting, errors }) => (
        <Form className="ui form" onSubmit={handleSubmit} autoComplete="off">
          <Header as="h2" content="Login" color="teal" textAlign="center" />
          <MyTextInput name="username" placeholder="Username" />
          <MyTextInput name="password" placeholder="Password" type="password" />
          <ErrorMessage
            name="error"
            render={() => (
              <Label
                style={{ marginBottom: 10 }}
                basic
                color="red"
                content={errors.error}
              />
            )}
          />
          <Button
            loading={isSubmitting}
            positive
            content="Login"
            type="submit"
            fluid
          />
        </Form>
      )}
    </Formik>
  );
});
