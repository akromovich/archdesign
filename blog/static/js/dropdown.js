(function () {
	var elDropdown = $(".nav__dropdown");
	var elDropdownToggler = $(".nav__lang");
	var elDropdownList = $(".nav__list--langs");

	var hideDropdown = (evt) => {
		if (
			!evt.target.classList.contains("tick") &&
			!evt.target.classList.contains("langclick")
		) {
			elDropdownList.classList.remove("dropdown--show");
			elDropdownToggler.classList.remove("active");
			elDropdownToggler.removeEventListener(
				"click",
				hideDropdownOnTogglerClick
			);
			document.removeEventListener("click", hideDropdown);
		}
	};

	var hideDropdownOnTogglerClick = () => {
		elDropdownList.classList.remove("dropdown--show");
		elDropdownToggler.classList.remove("active");
		elDropdownToggler.removeEventListener("click", hideDropdownOnTogglerClick);
		document.removeEventListener("click", hideDropdown);
	};

	var showDropdown = () => {
		elDropdownList.classList.add("dropdown--show");
		elDropdownToggler.classList.add("active");
		document.addEventListener("click", hideDropdown);
		elDropdownToggler.addEventListener("click", hideDropdownOnTogglerClick);
	};

	elDropdownToggler.addEventListener("click", showDropdown);

	// * lang select
	var setUzLang = () => {
		elDropdownToggler.querySelector(".lang__img").src = "../../../blog/static/flugs/uzb_flag_logo";
		elDropdownToggler.querySelector(".lang__text").textContent = "Uz";
		localStorage.setItem("lang", "uz");
	};

	var setRuLang = () => {
		elDropdownToggler.querySelector(".lang__img").src = "../../../blog/static/flugs/russia_flag_logo0";
		elDropdownToggler.querySelector(".lang__text").textContent = "Ru";
		localStorage.setItem("lang", "ru");
	};

	var setEnLang = () => {
		elDropdownToggler.querySelector(".lang__img").src =
			"../../../blog/static/flugs/enflug.jpg";
		elDropdownToggler.querySelector(".lang__text").textContent = "En";
		localStorage.setItem("lang", "en");
	};

	if (localStorage.getItem("lang")) {
		if (localStorage.getItem("lang") === "uz") {
			setUzLang();
		} else if (localStorage.getItem("lang") === "ru") {
			setRuLang();
		} else {
			setEnLang();
		}
	}

	var langSelect = (evt) => {
		if (!evt.target.classList.contains("tick")) {
			return;
		}

		var lang = evt.target.dataset.id;
		location.reload();

		if (lang === "uz") {
			setUzLang();
		} else if (lang === "ru") {
			setRuLang();
		} else {
			setEnLang();
		}
	};

	elDropdown.addEventListener("click", langSelect);

	// nav scroll effect
	var elNav = $('.nav');

	window.addEventListener('scroll', function () {
		if (window.scrollY > 225) {
			elNav.classList.add('nav-upgraded');
		} else {
			elNav.classList.remove('nav-upgraded');
		}
	});
})();

