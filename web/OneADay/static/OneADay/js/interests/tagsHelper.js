var tagsHelper = function () {
	$("#interest-tags").tagit({
		removeConfirmation: true,
		allowSpaces: true,
		tagLimit: 15,
		singleField: true,
		afterTagAdded: function(event, ui) { if(!ui.duringInitialization) return changeInterest('/add-interest/', ui.tagLabel) },
		afterTagRemoved: function(event, ui) { if(!ui.duringInitialization) return changeInterest('/remove-interest/', ui.tagLabel) }
	});

	function changeInterest(url, keyword) {
		//alert(keyword);
		postData = {
			keyword: keyword
		};

		$.post(url, postData, function(data, status) {
			if(status !== 'success') {
				return false;
			}
			console.log(status);
		});
	}

	// from https://docs.djangoproject.com/en/dev/ref/csrf/
	function getCookie(name) {
		var cookieValue = null;
		if (document.cookie && document.cookie != '') {
			var cookies = document.cookie.split(';');
			for (var i = 0; i < cookies.length; i++) {
				var cookie = jQuery.trim(cookies[i]);
				// Does this cookie string begin with the name we want?
				if (cookie.substring(0, name.length + 1) == (name + '=')) {
					cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
					break;
				}
			}
		}
		return cookieValue;
	}

	var csrftoken = getCookie('csrftoken');

	function csrfSafeMethod(method) {
		// these HTTP methods do not require CSRF protection
		return (/^(GET|HEAD|OPTIONS|TRACE)$/.test(method));
	}

	$.ajaxSetup({
		beforeSend: function(xhr, settings) {
			if (!csrfSafeMethod(settings.type) && !this.crossDomain) {
				xhr.setRequestHeader("X-CSRFToken", csrftoken);
			}
		}
	});
};