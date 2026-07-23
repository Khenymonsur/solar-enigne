document.addEventListener("DOMContentLoaded", () => {

    const state = document.getElementById("id_state");
    const lga = document.getElementById("id_lga");

    Object.keys(STATE_LGAS)
        .sort()
        .forEach(name => {

            state.add(
                new Option(name, name)
            );

        });

    state.addEventListener("change", function () {

        lga.innerHTML = "";

        lga.add(
            new Option("Select LGA", "")
        );

        if (!this.value) {
            return;
        }

        STATE_LGAS[this.value].forEach(item => {

            lga.add(
                new Option(item, item)
            );

        });

    });

});