module.exports = {
  root: true,
  env: {
    browser: true,
    jquery: true,
    node: true,
  },
  extends: [
    "eslint:recommended",
    "plugin:qunit/recommended",
    "standard",
    "prettier",
  ],
  parserOptions: {
    sourceType: "script",
  },
  plugins: ["prettier", "html", "qunit"],
}
