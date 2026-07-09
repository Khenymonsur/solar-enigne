document.addEventListener("DOMContentLoaded", function () {

    document.querySelectorAll(".clickable-table tbody tr").forEach(function (row) {

        row.addEventListener("click", function () {

            row.parentElement.querySelectorAll("tr").forEach(function (r) {
                r.classList.remove("table-active");
            });

            this.classList.add("table-active");

        });

    });

});