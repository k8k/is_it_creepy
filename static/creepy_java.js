$("#creep-button").click(
	function(evt)
	{
		alert("creepy")
		$.get('/creepy'),
		function(result) {
			alert(result)
		}
	});




  $("#creep-button").click(function (event) {

    // Make the URL for our AJAX request: this will be /result? follow by our form parameters
    // We'll use the jQuery .serialize() method on our form object.
    var url = "/result?" + $("#creep-form").serialize();

    // Print our URL to the JS console for debugging
    console.log(url);

    // Replace everything at #madlib-result with the result of our AJAX call
    $("#creep-result").load(url);
  })