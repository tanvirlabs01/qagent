export class LoginPage {
  constructor(private page) {}

  async navigate() {
    await this.page.goto("http://parabank.parasoft.com");
  }

  async login(username: string, password: string) {
    await this.page.fill('input[name="username"]', username);
    await this.page.fill('input[name="password"]', password);
    await this.page.click('input[type="submit"]');
  }

  async isLoginErrorVisible() {
    return this.page.locator("text=Invalid login").isVisible();
  }
}
