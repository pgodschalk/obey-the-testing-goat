window.Superlists = {}
window.Superlists.initialize = function () {
  $('input[name="text"]').on("keypress", function () {
    $(".has-error").hide()
  })

  $('input[name="text"]').on("click", function () {
    $(".has-error").hide()
  })
}
