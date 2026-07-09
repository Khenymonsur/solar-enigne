document.addEventListener("DOMContentLoaded", function () {

    const stateSelect = document.getElementById("id_state");
    const lgaSelect = document.getElementById("id_lga");

    if (!stateSelect || !lgaSelect) {
        return;
    }

    function populateLGAs(selected = "") {

        const state = stateSelect.value;

        lgaSelect.innerHTML = "";

        const defaultOption = document.createElement("option");
        defaultOption.value = "";
        defaultOption.textContent = "Select LGA";
        lgaSelect.appendChild(defaultOption);

        if (!STATE_LGAS[state]) {
            return;
        }

        STATE_LGAS[state].forEach(function (lga) {

            const option = document.createElement("option");

            option.value = lga;
            option.textContent = lga;

            if (lga === selected) {
                option.selected = true;
            }

            lgaSelect.appendChild(option);

        });

    }

    // Preserve saved LGA when editing
    const savedLGA = lgaSelect.dataset.selected || lgaSelect.value;

    populateLGAs(savedLGA);

    stateSelect.addEventListener("change", function () {

        populateLGAs();

    });

});