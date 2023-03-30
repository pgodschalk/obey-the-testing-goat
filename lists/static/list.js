// eslint-disable-next-line no-unused-vars
const initialize = function () {
  $('input[name="text"]').on("keypress", function () {
    $(".has-error").hide()
  })
}
