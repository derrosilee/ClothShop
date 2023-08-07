$(document).ready(function () {
  $('#signup-form').on('submit', function (e) {
    e.preventDefault();
    $.ajax({
      type: 'POST',
      url: '/accounts/signup/', // Replace with your signup URL
      data: $(this).serialize(),
      success: function (data) {
        if (data.success) {
          // Signup successful, display success message
          $('#success-message').text("Signup successful! Please check your email for verification.");
          $('#success-message').show();
        } else if (data.error) {
          // Signup error, display the error message
          $('#error-message').text(data.error);
        }
      },
      error: function (xhr, status, error) {
        // Handle error if necessary
      }
    });
  });
});
