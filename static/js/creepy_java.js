$("#creep-button").click(
	function(evt)
	{
		$.getJSON('/creepy', {
      your_age: $('input[name = "your_age"]').val(),
      other_age: $('input[name = "other_age"]').val()
    }, function(data){
      if (data.is_creepy) {
        // tell user they a creep
        //alert("Straight creep");
        $("#creep-result").text("Straight creep.")

      } else {
        
         $("#creep-result").text("You're alright.")
      }
    });
	});


  // $("#creep-button").click(function (event) {

  //   // Make the URL for our AJAX request: this will be /result? follow by our form parameters
  //   // We'll use the jQuery .serialize() method on our form object.
  //   var url = "/result?" + $("#creep-form").serialize();

  //   // Print our URL to the JS console for debugging
  //   console.log(url);

  //   // Replace everything at #madlib-result with the result of our AJAX call
  //   $("#creep-result").load(url);
  // });