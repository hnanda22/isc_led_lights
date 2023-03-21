$('#blue-button, #red-button, #green-button').click(function(e) {
    e.preventDefault();
    var color = $(this).attr('data-color');
    submitForm(color);
});

v
$('#rainbow-button').click(function(e) {
    e.preventDefault();
    // Send command to Arduino to activate rainbow animation
  });

function submitForm(color) {
    $.ajax({
        url: '/send-color',
        type: 'POST',
        data: {color: color},
        success: function(response) {
            console.log(response);
        }
    });
}