const search = document.getElementById("default-search");
const cards = document.querySelectorAll(".pokemon-card");

search.addEventListener("input", (valor) => {
    const searchValue = search.value.toLowerCase();
    let mostrarTodos = false;

    if (searchValue.length < 1) {
        mostrarTodos = true;
    }

    for (let card of cards) {
        const title = card.querySelector(".title-img-container h3");
        const pokemon = title.textContent.toLowerCase();

        if (mostrarTodos) {
            card.style.opacity = 1;

            continue;
        }

        if (pokemon.startsWith(searchValue)) {
            card.style.opacity = 1;
        } else {
            card.style.opacity = 0;
        }

    }

})