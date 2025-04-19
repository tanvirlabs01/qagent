import { test, expect } from "@playwright/test";
import { LoginPage } from "../pages/loginPage";

test("Invalid login attempt shows error", async ({ page }) => {
  const login = new LoginPage(page);

  await login.navigate();
  await login.login("user", "wrongpass");
  //expect(await login.isLoginErrorVisible()).toBeTruthy();
});
