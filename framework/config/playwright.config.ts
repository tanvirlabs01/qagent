import { defineConfig } from "@playwright/test";

export default defineConfig({
  testDir: "../tests",
  use: {
    baseURL: "http://parabank.parasoft.com",
    headless: false, // 👈 turn off headless
    viewport: { width: 1280, height: 800 },
    screenshot: "only-on-failure",
    video: "retain-on-failure",
  },
});
