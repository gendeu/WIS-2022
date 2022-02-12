var formData = new FormData();

$("#user_register").click(function(){
	formData.append('username', $('#username').val())
	formData.append('password', $('#password').val())
	formData.append('image',  $('#image')[0].files[0])
	formData.append('email', $('#email').val())
	formData.append('csrfmiddlewaretoken', $('input[name=csrfmiddlewaretoken]').val())
	$.ajax({
		type: 'POST',
		url: "/register",
		data: formData,
		cache: false,
		processData: false,
		contentType: false,
		enctype: 'multipart/form-data',
		success: function (res){
			alert("User has been added!" + res)
		},
		error: function(res) {
			console.log("ERROR:" + res)
		}
	})
})