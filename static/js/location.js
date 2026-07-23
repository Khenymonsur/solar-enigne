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

        const addressInput = document.getElementById("id_address");

        if (addressInput && window.google) {

            const autocomplete = new google.maps.places.Autocomplete(addressInput, {

                componentRestrictions: {
                    country: "ng"
                },

                fields: [
                    "formatted_address",
                    "geometry"
                ]

            });

            autocomplete.addListener("place_changed", () => {

                const place = autocomplete.getPlace();

                if (!place.geometry)
                    return;

                document.getElementById("id_latitude").value =
                    place.geometry.location.lat();

                document.getElementById("id_longitude").value =
                    place.geometry.location.lng();

            });

        }



    // Preserve saved LGA when editing
    const savedLGA = lgaSelect.dataset.selected || lgaSelect.value;

    populateLGAs(savedLGA);

    stateSelect.addEventListener("change", function () {

        populateLGAs();

    });

});