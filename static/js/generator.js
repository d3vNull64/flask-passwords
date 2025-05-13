document.addEventListener("DOMContentLoaded", () => {
	console.log("Generator script loaded...");

	document
		.getElementById("generatorForm")
		.addEventListener("submit", (event) => {
			event.preventDefault();
		});

	// NOTE: Sync range an number input and submit when value change
	const rangeLength = document.getElementById("rangeLen");
	const numberLength = document.getElementById("numberLen");

	rangeLength.addEventListener("input", () => {
		numberLength.value = rangeLength.value;
	});

	numberLength.addEventListener("input", () => {
		// regenerate button disable if length is out of range
		const numberValue = numberLength.value;
		if (
			numberLength.validity.badInput ||
			Number(numberValue) < 6 ||
			Number(numberValue) > 128
		) {
			numberLength.classList.add("is-invalid");
			document.getElementById("btn-gen").disabled = true;
		} else {
			if (numberLength.classList.contains("is-invalid")) {
				numberLength.classList.remove("is-invalid");
				document.getElementById("btn-gen").disabled = false;
			}
			rangeLength.value = numberValue;
		}
	});

	numberLength.addEventListener("change", () => {
		document.getElementById("generatorForm").submit();
	});

	rangeLength.addEventListener("change", () => {
		document.getElementById("generatorForm").submit();
	});

	// regenerate password button
	document.getElementById("btn-gen").addEventListener("click", () => {
		document.getElementById("generatorForm").submit();
	});

	// Submit with new option selected
	const btnsOptions = document.querySelectorAll(".btn-check");
	console.log(btnsOptions);
	btnsOptions.forEach((button) => {
		button.addEventListener("change", () => {
			document.getElementById("generatorForm").submit();
		});
	});

	// Copy generated password to clipboard
	document.querySelector("#btn-copy").addEventListener("click", () => {
		const password = document.querySelector("#txt-pass").value;
		navigator.clipboard
			.writeText(password)
			.then(() => {
				const buttonCopy = document.querySelector("#btn-copy");
				const originalText = buttonCopy.innerHTML;
				buttonCopy.innerHTML = '<i class="nf nf-fa-check me-2"></i>Copy';
				setTimeout(() => {
					buttonCopy.innerHTML = originalText;
				}, 3000);
			})
			.catch((err) => {
				alert("no se puedo", err);
			});
	});

	// console.log("12 →", !isNaN("12")); // true ✅
	// console.log("12s →", !isNaN("12s")); // false ❌
});
